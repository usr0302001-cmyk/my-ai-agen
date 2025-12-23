import streamlit as st
import google.generativeai as genai

# 1. ページ基本設定
st.set_page_config(page_title="Fanspot 見積エージェント", layout="wide")
st.title("🎯 Fanspot 案件見積・分析エージェント")

# 2. APIキー設定
# 最新のAPIキーを直接指定。余計な設定を省き、接続の安定性を最優先します。
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 3. 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("施策期間、当選者数などの情報をここに貼ってください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        # 【重要】モデル指定を最も標準的な形式に変更し、404エラーを回避します
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("専用ロジックで計算中..."):
                tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
                
                # あなたが設計した最強の見積ロジック
                logic = """
                あなたは熟練のプランナーです。以下の単価ルールを厳守して見積を作成してください。
                
                【初期費用】
                ・Fanspot 初期設定費用: 3,500,000円
                ・Fanspot レシート応募実装費: 1,000,000円
                ・Fanspot レシートOCR即時解析: 3,000,000円
                ・FanSpot インスタントウィン機能実装費: 3,000,000円
                ・目検作業費: 1,000円 × (当選者数の2倍)
                ・抽選費用: 50,000円/回
                
                【期間連動費用】
                ・Fanspot 月額費用: 650,000円 × 施策期間
                ・問合せ事務局対応費: 400,000円 × (施策期間 + 1ヶ月)
                ・FanSpot ページ更新費: 1,000,000円 × 更新回数
                """
                
                prompt = f"{logic}\n\n以下の条件で見積、ターゲット分析、ヒアリング事項を作成してください：\n{minutes}"
                
                # 生成実行
                response = model.generate_content(prompt)
                
                with tab1:
                    st.markdown(response.text)
                    st.divider()
                    st.warning("⚠️ **注釈：上記見積には、LINE配信費用および制作費用は含まれておりません。**")
                with tab2:
                    st.info("💡 詳細な分析結果は、上記の見積内容とあわせて確認してください。")
                with tab3:
                    st.info("📝 必要なヒアリング項目は見積結果の中に含まれています。")

        except Exception as e:
            st.error(f"接続エラーが発生しました。APIキーの有効化を確認してください: {str(e)}")
