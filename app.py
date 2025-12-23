import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta

# 1. ページ基本設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# 2. APIキーの設定
genai.configure(api_key="AIzaSyDW-1zglX-8H3X9Zt2dVYXX76L0dSoG46c")

# 3. 入力エリア
minutes = st.text_area("💼 議事録またはキャンペーン案をペーストしてください", height=200)

# 4. 実行ボタン
if st.button("🚀 分析・見積を開始する"):
    if minutes:
        # モデルの定義（パスを完全なものに修正）
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        with st.spinner("AIが戦略を立案中..."):
            # タブの作成
            tab1, tab2, tab3 = st.tabs(["📊 見積・条件案", "👥 ターゲット・ペルソナ", "📝 ヒアリングシート"])
            
            # 日付の計算
            deadline = (datetime.now() + timedelta(days=3)).strftime("%Y/%m/%d")
            
            # タブ1：見積
            with tab1:
                p1 = f"以下の議事録から、施策名、マストバイ条件、詳細な概算見積を作成してください。確認期限は{deadline}としてください。\n\n議事録：\n{minutes}"
                res1 = model.generate_content(p1)
                st.markdown(res1.text)
                
            # タブ2：ペルソナ
            with tab2:
                p2 = f"以下のキャンペーン施策について、詳細なペルソナ像（名前、年齢、悩み、生活習慣）を3名分作成してください。\n\n議事録：\n{minutes}"
                res2 = model.generate_content(p2)
                st.markdown(res2.text)
                
            # タブ3：ヒアリング
            with tab3:
                p3 = f"この施策を成功させるために、クライアントに確認すべき実務的な課題とヒアリング項目を5つ提案してください。\n\n議事録：\n{minutes}"
                res3 = model.generate_content(p3)
                st.markdown(res3.text)
    else:
        st.warning("議事録を入力してください。")
