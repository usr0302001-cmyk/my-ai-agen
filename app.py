import streamlit as st
import google.generativeai as genai
from datetime import datetime, timedelta

# 1. ページ基本設定
st.set_page_config(page_title="AI見積エージェント", layout="wide")
st.title("🎯 キャンペーン戦略・見積AIエージェント")

# 2. APIキーの設定（取得した新しいキーを反映済み）
genai.configure(api_key="AIzaSyAFsilIzfMzV2oBZWeanWEIkTYlH7ePwZ0")

# 3. 入力エリア
st.markdown("### 📋 スプレッドシートの内容をここに貼り付けてください")
minutes = st.text_area("スプレッドシートの情報を入力してください", height=250, placeholder="ここに情報を貼ってからボタンを押してください")

# 4. 実行ボタン
if st.button("🚀 分析・見積を開始する"):
    if not minutes.strip():
        st.warning("⚠️ 内容が空欄です！スプレッドシートから情報をコピーして貼り付けてください。")
    else:
        # モデルの定義
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        with st.spinner("AIが戦略を立案中..."):
            # タブの作成
            tab1, tab2, tab3 = st.tabs(["📊 見積・条件案", "👥 ターゲット・ペルソナ", "📝 ヒアリングシート"])
            
            # 日付の計算
            deadline = (datetime.now() + timedelta(days=3)).strftime("%Y/%m/%d")
            
            # 各タブの処理
            try:
                with tab1:
                    res1 = model.generate_content(f"以下の情報から、施策名、マストバイ条件、詳細な概算見積を作成してください。確認期限は{deadline}としてください。\n\n情報：\n{minutes}")
                    st.markdown(res1.text)
                with tab2:
                    res2 = model.generate_content(f"以下のキャンペーンについて、詳細なペルソナ像を3名分作成してください。\n\n情報：\n{minutes}")
                    st.markdown(res2.text)
                with tab3:
                    res3 = model.generate_content(f"クライアントに確認すべき課題とヒアリング項目を5つ提案してください。\n\n情報：\n{minutes}")
                    st.markdown(res3.text)
            except Exception as e:
                st.error(f"エラーが発生しました。入力内容やAPI設定を確認してください: {e}")
