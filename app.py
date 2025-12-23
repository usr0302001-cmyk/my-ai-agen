import streamlit as st
import google.generativeai as genai

# ページ設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# APIキー設定
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 入力エリア
st.markdown("### 📋 スプレッドシートの情報を貼り付けてください")
minutes = st.text_area("「施策期間」「当選者数」などの情報をここに貼ってください", height=200)

if st.button("🚀 見積・分析を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！情報を入力してください。")
    else:
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        with st.spinner("貴社専用ロジック（ Fanspot / 事務局＋1ヶ月 ）で計算中..."):
            tab1, tab2, tab3 = st.tabs(["📊 詳細見積書", "👥 ターゲット分析", "📝 ヒアリング事項"])
            
            # あなたの作成した最強ロジックを反映
            logic = """
            あなたは熟練のキャンペーンプランナーです。
            以下の【貴社専用単価ルール】を厳守し、計算式を明示して見積を作成してください。
            金額はすべて税抜です。

            【1. 絶対にかかる初期費用】
            ・Fanspot 初期設定費用: 3,500,000円
            ・Fanspot レシート応募実装費: 1,000,000円
            ・Fanspot レシートOCR即時解析: 3,000,000円
            ・FanSpot インスタントウィン機能実装費: 3,000,000円（※有りの場合のみ）
            ・目検作業費: 1枚1,000円。想定応募数は当選数の2倍として算出（当選1万なら2万枚）。
            ・抽選費用: 50,000円/回

            【2. CP期間に連動する費用】
            ・Fanspot 月額費用: 650,000円 × 施策期間(月数)
            ・問合せ事務局対応費: 400,000円 × (施策期間 + 1ヶ月)
              ※当選連絡・発送作業を含めるため、必ず期間に1ヶ月加算して計算すること。
            ・FanSpot 実装期間中のページ更新費: 1,000,000円 × 更新回数

            【出力形式】
            「合計費用」を明示し、最後に「結論」として企画の成立可否に関するコメントを添えてください。
            """
            
            try:
                with tab1:
                    res1 = model.generate_content(f"{logic}\n\n以下の情報を元に算出してください：\n{minutes}")
                    st.markdown(res1.text)
                    st.divider()
                    st.warning("⚠️ **注釈：上記見積には、LINE配信費用およびクリエイティブ制作費用は含まれておりません。**")
                
                with tab2:
