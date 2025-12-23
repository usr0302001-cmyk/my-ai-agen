import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Fanspot見積エージェント", layout="wide")
st.title("🎯 Fanspot 案件見積エージェント")

# 最新キーに更新
genai.configure(api_key="AIzaSyDW-1zglX-8H3X9Zt2dVYXX76L0dSoG46c")

# 入力項目
period = st.number_input("施策期間 (月数)", min_value=1, value=2)
winners = st.number_input("当選者数", min_value=0, value=10000)
is_iw = st.radio("インスタントウィン", ["有り", "無し"])
update = st.number_input("ページ更新回数", min_value=0, value=1)
has_ocr = st.radio("OCR解析機能", ["有り", "無し"])

if st.button("🚀 見積を実行"):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 事務局期間と目検費をコード側で事前計算
        jimukyoku_period = period + 1
        meken_cost = winners * 2 * 1000
        
        logic = f"""
        熟練のプランナーとして見積書を作成してください。
        【条件】期間:{period}ヶ月 / 当選:{winners}名 / IW:{is_iw} / OCR:{has_ocr} / 更新:{update}回
        【単価（税抜）】
        1. 初期費用
           - Fanspot初期設定：3,500,000円
           - レシート応募実装：1,000,000円
           - OCR解析：3,000,000円（※有りの場合）
           - IW実装：3,000,000円（※有りの場合）
           - 目検作業費：{meken_cost:,}円（当選の2倍×1,000円）
           - 抽選費用：50,000円
        2. 運用費用
           - 月額費用：{650000 * period:,}円（65万×期間）
           - 事務局費：{400000 * jimukyoku_period:,}円（40万×{jimukyoku_period}ヶ月）
           - ページ更新費：{1000000 * update:,}円（100万×回数）
        """
        
        res = model.generate_content(logic)
        st.markdown("---")
        st.markdown(res.text)
        st.warning("⚠️ 注釈：LINE配信費用および制作費用は含まれておりません。")

    except Exception as e:
        st.error(f"接続エラー: {e}")
