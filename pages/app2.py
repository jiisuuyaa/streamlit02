import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

### 검색창 만들고 입력 받아서 이미지 출력

# 검색창 (내코드)
search = st.text_input("♥검색★")

# if search == "짱구는 못말려":
#     st.image('https://i.imgur.com/t2ewhfH.png')
# elif search == "몬스터":
#     st.image('https://i.imgur.com/ECROFMC.png')
# elif search == "릭앤모티":
#     st.image('https://i.imgur.com/MDKQoDc.jpg')

# 선생님코드 _ for문 사용 
for ani in ani_list:
    if search in ani : 
        #ani_list에서 특정 문자열을 포함한 인덱스
        img_idx = ani_list.index(ani)
if search == "":
    st.write('찾는 애니메이션의 이미지가 없습니다.')
else:
    st.image(img_list[img_idx])

