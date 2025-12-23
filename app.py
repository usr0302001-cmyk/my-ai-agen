import streamlit as st
import google.generativeai as genai

# 1. 基本設定
st.set_page_config(page_title="Fanspot見積エージェント", layout="wide")
st.title("🎯 Fanspot 案件見積エージェント")

# 2. APIキー設定
genai.configure(api_key="AIzaSyDW-1zglX-8H3X9Zt2dVYXX76L0dSoG46c")

# 3. 入力画面
st.markdown("### 📋 キャンペーン条件を入力してください")
col1, col2 = st.columns(2)
with col1:
    period = st.number_input("施策期間 (月数)", min_value=1, value=2)
    winners = st.number_input("当選者数", min_value=0, value=10000)
    update = st.number_input("ページ更新回数", min_value=0, value=1)
with col2:
    is_iw = st.radio("インスタントウィン", ["有り", "無し"])
    has_ocr = st.radio("OCR解析機能", ["有り", "無し"])

# 4. 見積実行ボタン
if st.button("🚀 見積を実行"):
    try:
        # 【解決策】gemini-1.5-flashで404が出るため、互換性の高い'gemini-pro'に変更します
        model = genai.GenerativeModel('gemini-pro')
        
        # 事務局期間と目検費を事前にPython側で計算（AIの計算ミスを防ぐ）
        jimukyoku_months = period + 1
        meken_count = winners * 2
        meken_cost = meken_count * 1000
        
        logic = f"""
        あなたはプロのプランナーとして、以下の条件で正確な見積書を作成してください。
        
        【条件】
        ・施策期間：{period}ヶ月
        ・当選者数：{winners}名（目検対象：{meken_count}枚）
        ・インスタントウィン：{is_iw}
        ・OCR機能：{has_ocr}
        ・更新回数：{update}回

        【単価ルール（すべて税抜）】
        1. 初期費用
           - Fanspot初期設定：3,500,000円
           - レシート応募実装：1,000,000円
           - OCR解析実装：{"3,000,000円" if has_ocr == "有り" else "0円"}
           - インスタントウィン実装：{"3,000,000円" if is_iw == "有り" else "0円"}
           - 目検作業費：{meken_cost:,}円（{meken_count:,}枚 × 1,000円）
           - 抽選費用：50,000円
        2. 運用費用
           - 月額費用：{650000 * period:,}円（65万 × {period}ヶ月）
           - 事務局費
