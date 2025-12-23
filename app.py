import streamlit as st
import google.generativeai as genai

# 1. ページ基本設定
st.set_page_config(page_title="Fanspot 見積エージェント", layout="wide")
st.title("🎯 Fanspot 案件見積・分析エージェント")

# 2. APIキー設定
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 3. 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("「施策期間」「当選者数」などの情報をここに貼ってください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        # モデル呼び出しの安定化（404エラーを物理的に回避する設定）
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        with st.spinner("専用ロジックで計算中..."):
            tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
            
            logic = """
            あなたは熟練のプランナーです。以下の単価ルールを厳守して見積を作成してください。
            金額はすべて税抜です。
            
            【1. 絶対にかかる初期費用】
            ・Fanspot 初期設定費用: 3,500,000円
            ・Fanspot レシート応募実装費: 1,000,000円
            ・Fanspot レシートOCR即時解析: 3,000,000円
            ・FanSpot インスタントウィン機能実装費: 3,000,000円（※有りの場合のみ）
            ・目検作業費: 1,000円 × (当選者数の2倍)
            ・抽選費用: 50,000円/回

            【2. CP期間に連動する費用】
            ・Fanspot 月額費用: 650,000円 × 施策期間(月数)
            ・問合せ事務局対応費: 400,000円 × (施策期間 + 1ヶ月)
            ・FanSpot 実装期間中のページ更新費: 1,000,000円 × 更新回数
            """
            
            try:
                # 連結プロンプトによる一括生成
                full_prompt = f"{logic}\n\n以下の条件で見積、ターゲット分析、ヒアリング事項を日本語で作成してください：\n{minutes}"
                response = model.generate_content(full_prompt)
                
                # 結果をタブごとに整理して表示（AIが構造的に出力するように指示）
                with tab1:
                    st.markdown(response.text)
                    st.divider()
                    st.warning("⚠️ **注釈：上記見積には、LINE配信費用および制作費用は含まれておりません。**")
                
                with tab2:
                    st.info("💡 見積結果に基づいたターゲット分析を上記タブ1と併せて確認してください。")
                    
                with tab3:
                    st.info("📝 必要なヒアリング事項は上記の見積内容に含まれています。")

            except Exception as e:
                # エラーメッセージをより詳細に出力して原因を特定しやすくする
                st.error(f"実行中にエラーが発生しました。設定を再確認しています: {str(e)}")
