import streamlit as st
import google.generativeai as genai

# 1. ページ基本設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# 2. APIキー設定
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 3. 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("「施策期間」「当選者数」などの情報をここに貼ってください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        # モデル名を「gemini-1.5-flash」のみに修正（これで404エラーを回避します）
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("専用ロジックで計算中..."):
            tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
            
            logic = """
            あなたは熟練のプランナーです。以下の単価ルールを厳守して見積を作成してください。
            【初期費用】
            ・Fanspot 初期設定費用: 3,500,000円
            ・Fanspot レシート応募実装費: 1,000,000円
            ・Fanspot レシートOCR即時解析: 3,000,000円
            ・FanSpot インスタントウィン機能実装費: 3,000,000円（※有りの場合）
            ・目検作業費: 1,000円 × (当選者数の2倍)
            ・抽選費用: 50,000円/回
            【期間連動費用】
            ・Fanspot 月額費用: 650,000円 × 施策期間
            ・問合せ事務局対応費: 400,000円 × (施策期間 + 1ヶ月)
            ・FanSpot ページ更新費: 1,000,000円 × 更新回数
            """
            
            try:
                # すべての回答を生成
                res1 = model.generate_content(f"{logic}\n\n条件：\n{minutes}")
                res2 = model.generate_content(f"詳細なターゲットペルソナを3名作成して：\n{minutes}")
                res3 = model.generate_content(f"クライアントへのヒアリング項目を5つ提案して：\n{minutes}")

                with tab1:
                    st.markdown(res1.text)
                    st.divider()
                    st.warning("⚠️ **注釈：上記見積には、LINE配信費用および制作費用は含まれておりません。**")
                with tab2:
                    st.markdown(res2.text)
                with tab3:
                    st.markdown(res3.text)
                    
            except Exception as e:
                st.error(f"実行中にエラーが発生しました。時間をおいて再度お試しください: {e}")
