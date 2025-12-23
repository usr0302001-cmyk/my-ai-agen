import streamlit as st

# 1. ページ基本設定
st.set_page_config(page_title="Fanspot 見積システム", layout="wide")
st.title("🎯 Fanspot 案件見積・分析エージェント")

# 2. 入力フォーム（サイドバー）
st.sidebar.header("📋 キャンペーン条件を入力")
period = st.sidebar.number_input("施策期間 (月数)", min_value=1, value=2)
winners = st.sidebar.number_input("当選者数", min_value=0, value=10000, step=1000)
is_iw = st.sidebar.radio("インスタントウィン", ["有り", "無し"])
update_count = st.sidebar.number_input("ページ更新回数", min_value=0, value=1)
has_ocr = st.sidebar.radio("OCR解析機能", ["有り", "無し"])

# 3. 計算実行
if st.sidebar.button("🚀 見積もりを算出する"):
    # 事務局期間と枚数の算出
    jimukyoku_months = period + 1
    meken_count = winners * 2
    
    # 金額計算
    init_setup = 3500000
    receipt_impl = 1000000
    ocr_cost = 3000000 if has_ocr == "有り" else 0
    iw_cost = 3000000 if is_iw == "有り" else 0
    meken_cost = meken_count * 1000
    lottery_cost = 50000
    
    monthly_system = 650000 * period
    jimukyoku_cost = 400000 * jimukyoku_months
    update_cost = 1000000 * update_count
    
    total_cost = (init_setup + receipt_impl + ocr_cost + iw_cost + meken_cost + lottery_cost + 
                  monthly_system + jimukyoku_cost + update_cost)

    # 結果表示
    st.markdown("### 📊 御見積書（概算）")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        #### ■ 初期費用
        - Fanspot 初期設定費用: 3,500,000円
        - Fanspot レシート応募
