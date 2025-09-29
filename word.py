import streamlit as st
import random

st.set_page_config(page_title="ワードスナイパー", layout="centered")

HIRAGANA = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
THEMES = ["果物", "動物", "食べ物", "国名", "乗り物"]

# ---------------------------
# セッション初期化
# ---------------------------
if "char" not in st.session_state:
    st.session_state.char = ""
if "theme" not in st.session_state:
    st.session_state.theme = ""
if "scores" not in st.session_state:  # 名前→スコアの辞書
    st.session_state.scores = {}

st.title("🎯 ワードスナイパー")

# ---------------------------
# プレイヤー名入力
# ---------------------------
player_name = st.text_input("プレイヤー名を入力してください（必須）")

def draw_card():
    st.session_state.char = random.choice(HIRAGANA)
    st.session_state.theme = random.choice(THEMES)

# ---------------------------
# ボタン操作
# ---------------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("カードをめくる", use_container_width=True):
        if player_name:
            draw_card()
        else:
            st.warning("名前を入力してください")

# 「ポイント加算」を押した回数だけ自動でスコア更新
with col2:
    if st.button("ポイント加算", use_container_width=True):
        if player_name:
            # クリック1回ごとに +1
            st.session_state.scores[player_name] = st.session_state.scores.get(player_name, 0) + 1
        else:
            st.warning("名前を入力してください")

# ---------------------------
# 表示
# ---------------------------
if st.session_state.char:
    st.markdown("---")
    st.markdown(
        f"<div style='font-size:80px;text-align:center;'>{st.session_state.char}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='font-size:40px;text-align:center;'>お題：{st.session_state.theme}</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")

# ---------------------------
# スコア一覧
# ---------------------------
if st.session_state.scores:
    st.subheader("📊 スコア（クリック回数）")
    for name, score in sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{name}** ： {score} 回")
