import streamlit as st
import google.generativeai as genai

# 1. ページ基本設定
st.set_page_config(page_title="Fanspot 見積エージェント", layout="wide")
st.title("🎯 Fanspot 案件見積・分析エージェント")

# 2. 最新のAPIキーを設定
# 先ほどいただいた新しいキーを反映しました
genai.configure(api_key="AIzaSyDW-1zglX-8H3X9Zt2dVYXX76L0dSoG46c")

# 3. 入力エリア
st.markdown("### 📋 キャンペーン情報を貼り付けてください")
minutes = st.text_area("「2ヶ月」「当選1万人」などの情報をここに貼ってください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        # モデル呼び出しを最新の安定版に固定
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("専用ロジックで計算中..."):
                tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
                
                # あなたが設計した精緻な単価ロジック
                logic = """
                あなたは熟練のプランナーです。以下の単価ルール（税抜）を厳守して見積を作成してください。
                【初期費用】
                ・Fanspot 初期設定：3,500,000円
                ・レシート応募実装：1,000,000円
                ・OCR解析：3,000,000円
                ・インスタントウィン実装：3,000,000円（※有りの場合）
                ・目検作業費：当選者数の2倍 × 1,000円
                ・抽選費用：50,000円
                【運用費用】
                ・月額費用：650,000円 × 期間
                ・事務局費：400,000円 × (期間 + 1ヶ月)
                ・ページ更新：1,000,000円 × 回数
                """
                
                # AIに依頼
                response = model.generate_content(f"{logic}\n\n条件：\n{minutes}")
                
                with tab1:
                    st.markdown("### 📊 自動生成された見積書")
                    st.write(response.text)
                    st.divider()
                    st.warning("⚠️ **注釈：上記見積には、LINE配信費用および制作費用は含まれておりません。**")
                
                with tab2:
                    st.info("💡 ターゲット分析は上記の見積内容とあわせて確認してください。")
                    
                with tab3:
                    st.info("📝 必要なヒアリング項目は見積結果の中に含まれています。")

        except Exception as e
