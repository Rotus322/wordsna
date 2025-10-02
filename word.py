import streamlit as st
import random

st.markdown(
    """
    <h1 style='
        font-size:35px;      /* 文字サイズ(px) */
        text-align:center;   /* 中央揃え */
        color:#ff4b4b;       /* 文字色（赤系） */
        font-family:"Comic Sans MS", cursive; /* フォント指定 */
        margin-bottom:10px;  /* 下の余白 */
    '>
    🎯 ワードスナイパー
    </h1>
    """,
    unsafe_allow_html=True
)
HIRAGANA = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞだでどばびぶべぼぱぴぷぺぽWRTYPSDGHJKZVBNM")
THEMES   = ["果物",
            "動物",
            "和食",
            "国名",
            "乗り物",
            "お菓子",
            "都道府県",
            "学校で使うもの",
            "夏と言えば",
            "春と言えば",
            "冬と言えば",
            "秋と言えば",
            "職業",
            "スポーツ",
            "野菜",
            "キャラクター",
            "小学校の時に流行ったもの",
            "高校時代に流行ったもの",
            "チェーン店",
            "理系用語",
            "医療用語",
            "物語",
            "怖いもの",
            "芸能人",
            "歴史で習った言葉",
            "市区町村",
            "遊び",
            "観光地",
            "一日の中で一回は触るもの",
            "苗字",
            "コンビニに売ってるもの",
            "今書いてる文字",
            "飲食店あるある",
            "家にあるもの",
            "便利なもの",
            "かわいいもの",
            "あかいもの",
            "青いもの",
            "きいろいもの",
            "しろいもの",
            "黒いもの",
            "触れないもの",
            "今日触ったもの",
            "三日坊主になりやすいもの",
            "7文字以上の言葉",
            "曲名",
            "副教科（音楽、美術、保健・体育、技術・家庭）で出てきた言葉",
            "子供が好きなもの",
            "男のひと（男の子）が好きなもの",
            "女のひと（女の子）が好きなもの",
            "一度はしてみたいこと",
            "相手の尊敬できるとこ",
            "かたいもの",
            "四角いもの",
            "海の生き物",
            "身に着けるもの",
            "キッチン用品",
            "生きるために必要なもの",
            "細長いもの",
            "やわらかいもの",
            "楽器",
            "体の一部",
            "目に見えないもの",
            "太いもの",
            "首都",
            "とがったもの",
            "丸いもの",
            "県庁所在地",
            "海外の料理",
            "食べ物",
            "冷たいもの",
            "熱いもの",
            "はやいもの",
            "遅いもの",
            "遊び",
            "小さいもの",
            "東京ドームより広い場所",
            "生で食べられるもの",
            "無人島で役に立つもの",
            "お金で変えないもの",
            "気持ちを表す言葉",
            "持つことができないもの",
            "持つことができるもの",
            "虫",
            "飲み物",
            "危険な場所",
            "二文字のもの",
            "調味料",
            "電子機器",
            "キラキラしたもの",
            "スイーツ",
            "鍋の具になるもの",
            "告白する場所",
            "ことわざ・慣用句",
            "四字熟語",
            "旅行に持っていくもの",
            "駅名",
            "冷蔵庫に入れるもの",
            "さらさらしたもの",
            "ざらざらしたもの",
            "揺れるもの",
            "穴が開いているもの",
            "ネットで買えないもの",
            "薄いもの",
            "居酒屋のメニューにあるもの",
            "弾むもの",
            "ごはんにのせるもの",
            "300円で買える",
            "3㎝より小さいもの",
            "自動販売機に売っているもの",
            "高いもの",
            "見ると幸せになるもの",
            "水に浮くもの",
            "光るもの",
            "子供には早いもの",
            "いざというときに頼りになるもの",
            "10分でできること",
            "たくさん種類のあるもの",
            "包まれているもの",
            "いま目で見えるところにあるもの",
            "透明なもの",
            "ビルから落としても壊れないもの",
            "してはいけないこと",
            "感謝されること",
            "未来にできそうなもの",
            "未来になくなりそうなもの",
            "数字が入る言葉",
            "宇宙に関係するもの",
            "一人ではできないこと",
            "見たことないけど知っているもの",
            "「ん」で終わるもの",
            "うるさいもの",
            "静かなもの",
            "うれしいときにすること",
            "緊張すること",
            "恥ずかしいこと",
            "空を飛べるもの",
            "逆から読んでも意味がある言葉",
            "国語で習った言葉",
            "時代・元号",
            "驚くこと・もの",
            "ひとつ前の文字",
            "性格を表す言葉",
            "大学名",
            "部活",
            "ナンバープレートにある地名",
            "YouTuber",
            "歌手",
            "アプリ",
            "木でできてるもの",
            "元素",
            "お祭りにあるもの",
            "恋人と付き合う上で必要なこと",
            "アイスの名前",
            "お寿司のネタ",
            "こんな上司は嫌だ。どんな上司？",
            "変な人だと思う特徴",
            "異性をかわいい・かっこいいと思うもの・とき",
            "色"]
# ---------------------------
# セッション初期化
# ---------------------------
if "char" not in st.session_state:
    st.session_state.char = ""
if "theme" not in st.session_state:
    st.session_state.theme = ""
if "players" not in st.session_state:
    st.session_state.players = []          # 登録済プレイヤー名リスト
if "scores" not in st.session_state:
    st.session_state.scores = {}           # {名前: スコア}

 
 
st.subheader("お題に対して出てきた文字で答えよう！")
st.markdown(
    """
    <h1 style='
        font-size:15px;      /* 文字サイズ(px) */
        text-align:center;   /* 中央揃え */
        color:#ff4b4b;       /* 文字色（赤系） */
        font-family:"Comic Sans MS", cursive; /* フォント指定 */
        margin-bottom:10px;  /* 下の余白 */
    '>
    ※アルファベットの場合はその文字から始まる英単語かひらがなで〇行のどれでもよいとする<br>例：R→ラ行orR....
    </h1>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# プレイヤー登録
# ---------------------------
st.subheader("プレイヤー登録")
new_name = st.text_input("新しいプレイヤー名")
if st.button("追加"):
    name = new_name.strip()
    if name:
        if name not in st.session_state.players:
            st.session_state.players.append(name)
            st.session_state.scores[name] = 0
        else:
            st.warning("その名前は既に登録されています")

# ---------------------------
# カードめくり
# ---------------------------
def draw_card():
    st.session_state.char = random.choice(HIRAGANA)
    st.session_state.theme = random.choice(THEMES)

if st.button("カードをめくる", use_container_width=True):
    if st.session_state.players:
        draw_card()
    else:
        st.warning("プレイヤーを登録してください")

# ---------------------------
# カード表示
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
# プレイヤーごとのポイント加算ボタン
# ---------------------------
if st.session_state.players:
    st.subheader("プレイヤー別ポイント加算")
    # 2列ずつ並べる例（人数が多い場合は横スクロール）
    cols = st.columns(2)
    for i, name in enumerate(st.session_state.players):
        col = cols[i % 2]
        with col:
            if st.button(f"＋1点 {name}", key=f"add_{name}"):
                st.session_state.scores[name] += 1

# ---------------------------
# スコアボード
# ---------------------------
if st.session_state.scores:
    st.subheader("📊 スコアボード")
    for name, score in sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True):
        st.write(f"**{name}** ： {score} pt")
