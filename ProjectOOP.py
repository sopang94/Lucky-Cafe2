import streamlit as st
import pandas as pd
import streamlit as st
import random
    
tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(['หน้าหลัก', 'เมนูน้ำ','เมนูกาเเฟ','เมนูของหวาน','สุ่มเมนู','รีวิว','ติดต่อเรา',])


with tab1:
    st.title('Lucky Cafe')
    st.image('https://i.pinimg.com/564x/40/9d/8c/409d8c9d59034f7a726e5ead0c1fb0f4.jpg')
    st.caption('ยินดีต้อนรับสู่ Lucky Cafe ร้านคาเฟ่เล็ก ๆ สไตล์มินิมอล แต่ความอร่อยล้นแก้ว')
    st.caption('เปิดให้บริการ 10:00-19:00 น. จ-ศ หยุดทุกวันอาทิตย์')
    st.header('เมนูพิเศษจากทางร้าน')
    left, c, c1, c2, right = st.columns(5)
    left.markdown('เมนูน้ำ')
    c.markdown('')
    c1.markdown('')
    c2.markdown('')
    
    col1, col2, col3, col4 = st.columns(4)
    col1.image('https://i.pinimg.com/564x/82/a5/22/82a5225f0817fda5c26e7709f08f63bc.jpg', width=150, caption='สตอเบอรี่นมสด (45)')
    col2.image('https://i.pinimg.com/564x/87/56/92/875692c39820a41aedc3e9148d906190.jpg', width=150, caption='กาแฟเลิฟ (70)')
    col3.image('https://i.pinimg.com/236x/59/2b/bc/592bbc9cfd37515c57f3799131a2f217.jpg', width=120, caption='ส้มรักพ่อ (65)')
    col4.image('https://i.pinimg.com/564x/f4/d4/dc/f4d4dc71b20a6cd45f75730ef86937c9.jpg', width=125, caption='ชาเขียวเยียวยาใจ (45)')
    left1, c3, c4, c5, right2 = st.columns(5)
    left1.markdown('เมนูของหวาน')
    c3.markdown('')
    c4.markdown('')
    c5.markdown('')

    co1, co2, co3, co4 = st.columns(4)
    co1.image('https://i.pinimg.com/564x/8f/82/74/8f827404a2b3dd9d1309fd31b170990a.jpg', width=150,
              caption='ที่ยิ้มไม่ได้เจ้าชู้ (25)')
    co2.image('https://i.pinimg.com/564x/68/95/d4/6895d413dbf6e74ae450ffa6d4f7487b.jpg', width=150,
              caption='พุดดิ้งนมสด (25)')
    co3.image('https://i.pinimg.com/564x/10/88/a0/1088a07881acbf9692080fd037c65d9d.jpg', width=150,
              caption='เค้กเลม่อน (25)')
    co4.image('https://i.pinimg.com/564x/17/8b/e8/178be8b48a6ea8c97bf972c5e55154ad.jpg', width=150,
              caption='สโนบราวน์ (25)')

with tab2:
    water1 , water2 , water3 = st.columns(3)

    with water1:
        st.subheader("ชาไทย (Thai Tea)")
        st.image("https://i.pinimg.com/564x/fd/be/17/fdbe1703e279924625d164a7f7e2643f.jpg")
        st.write("45 บาท")

    with water2:
        st.subheader("ชาชมพู (Roselle Tea)")
        st.image("https://i.pinimg.com/564x/d2/24/91/d22491eb64c8e3de35583a5d81e930d4.jpg")
        st.write("40 บาท")

    with water3:
        st.subheader("ชาเขียว (Green tea)")
        st.image("https://i.pinimg.com/736x/32/3b/33/323b333b6edc8a1d811e45dc7231a1e9.jpg")
        st.write("50 บาท")

    water4 , water5 , water6 = st.columns(3)

    with water4:
        st.subheader("ชาเย็นไข่มุก (Iced Bubble Tea)")
        st.image("https://i.pinimg.com/564x/5e/bd/27/5ebd27adc0f326cfd0bd2bb1b5b99b29.jpg")
        st.write("45 บาท")

    with water5:
        st.subheader("นมสด (Milk)")
        st.image("https://i.pinimg.com/564x/02/4f/9d/024f9d3b6a7ddd0eaddc758a21bbaf56.jpg")
        st.write("45 บาท")
    
    with water6:
        st.subheader("น้ำเปล่า (Water)")
        st.image("https://i.pinimg.com/564x/64/b3/65/64b365d7c4b41f5a7d1ca71094b9297e.jpg")
        st.write("20 บาท")

with tab2:
    water7, water8, water9 = st.columns(3)

    with water7:
        st.subheader("น้ำส้ม (Orange Juice)")
        st.image("https://i.pinimg.com/564x/36/82/4e/36824eaf7777ee61865a43ad9646c4e1.jpg")
        st.write("35 บาท")

    with water8:
        st.subheader("น้ำมะพร้าว (Coconut Water)")
        st.image("https://i.pinimg.com/564x/33/58/db/3358db9d6ba60a421fce93677ebb6460.jpg")
        st.write("30 บาท")

    with water9:
        st.subheader("น้ำแอปเปิ้ล (Apple Juice)")
        st.image("https://i.pinimg.com/564x/db/bd/72/dbbd726d3ecafa00ec1fdad8baf1d99b.jpg")
        st.write("40 บาท")

    water10 , water11 , water12 = st.columns(3)
    
    with water10:
        st.subheader("โกโก้ (Cocoa)")
        st.image("https://i.pinimg.com/564x/bc/72/e4/bc72e425fe957e6c481f1479ea4e2c8b.jpg")
        st.write("45 บาท")
    
    with water11:
        st.subheader("ชาดำ (Black Tea)")
        st.image("https://i.pinimg.com/564x/06/6c/c8/066cc8984d807bf4b9fbc9d5bf6ae952.jpg")
        st.write("35 บาท")

    with water12:
        st.subheader("ชามะลิ (Jasmine tea)")
        st.image("https://i.pinimg.com/564x/82/20/6f/82206f450e59364fa7be7bed4606d0c4.jpg")
        st.write("40 บาท")
        
with tab3:
    water1 , water2 , water3 = st.columns(3)

    with water1:
        st.subheader("เอสเพรสโซ่ (Espresso)")
        st.image("https://i.pinimg.com/564x/5c/f7/9c/5cf79ce28f2ebd3f97ffff1fadd0d6f9.jpg")
        st.write("45 บาท")

    with water2:
        st.header("อเมริกาโน่ (Americano)")
        st.image("https://i.pinimg.com/564x/93/50/8d/93508dfce47fd1d677be051d6527a0b4.jpg")
        st.write('55 บาท')

    with water3:
        st.header("ลาเต้ (Latte)")
        st.image("https://i.pinimg.com/564x/2b/da/de/2bdadea984bfafb8c65c52f00bcc7ef7.jpg")
        st.write('65 บาท')

    water4 , water5 , water6 = st.columns(3)

    with water4:
        st.subheader("คาปูชิโน่ (Cappuccino)")
        st.image("https://i.pinimg.com/564x/2d/d4/cf/2dd4cfb175eb4cb2e17bf5bc0c8b59cc.jpg")
        st.write("60 บาท")

    with water5:
        st.header("มอคค่า (Mocha)")
        st.image("https://i.pinimg.com/564x/ec/65/9e/ec659ee19d12b2890931d575f6d13e1a.jpg")
        st.write('70 บาท')

    with water6:
        st.header("มัคคิอาโต้ (Macchiato)")
        st.image("https://i.pinimg.com/564x/97/ec/f7/97ecf715edbaf993f2c65c4e6123f4df.jpg")
        st.write('50 บาท')
    water7 , water8 , water9 = st.columns(3)

    with water7:
        st.subheader("อัฟโฟกาโต้ (Hot/Cold Affogato)")
        st.image("https://i.pinimg.com/564x/79/02/86/7902868d58cb28083caf50306bc2af1f.jpg")
        st.write("80 บาท")

    with water8:
        st.header("ริซเตรทโต้ (Ristretto)")
        st.image("https://i.pinimg.com/564x/30/e4/fa/30e4fa735cb021afb7bbb4cba939f499.jpg")
        st.write('50 บาท')

    with water9:
        st.header("ไอซ์ บริว (Iced Brew)")
        st.image("https://i.pinimg.com/564x/2a/25/1e/2a251ede65e506f664936d7dc270642b.jpg")
        st.write('65 บาท')

with tab4:
    
        water1 , water2 , water3 = st.columns(3)

        with water1:
            st.subheader("เค้กช็อกโกแลต")
            st.image("https://i.pinimg.com/736x/69/66/fc/6966fce4b3153c05b176e21fe37d9b4a.jpg")
            st.write("39 บาท")

        with water2:
            st.header("ไอศกรีม")
            st.image("https://i.pinimg.com/564x/6d/e2/ce/6de2ce991c66b6136eb72243f12c449e.jpg")
            st.write('25 บาท')

        with water3:
            st.header("บราวนี่")
            st.image("https://i.pinimg.com/564x/68/8a/4d/688a4d8dd8ed6f08d51728c2257ffb19.jpg")
            st.write('70 บาท')

        water4 , water5 , water6 = st.columns(3)

        with water4:
            st.subheader("เค้กสตรอเบอร์รี่")
            st.image("https://i.pinimg.com/564x/9d/cf/c1/9dcfc133a1a95384d456c6346837780a.jpg")
            st.write("199 บาท")

        with water5: 
            st.header("พายแอปเปิ้ล")
            st.image("https://i.pinimg.com/564x/dd/de/26/ddde26a3252888d4f505fcf2b63751f2.jpg")
            st.write('99 บาท')

        with water6:
            st.header("คุโรบิสครีม")
            st.image("https://i.pinimg.com/564x/e7/f6/a6/e7f6a66343620a1d816255e90f5e78e6.jpg")
            st.write('70 บาท')
            
        water7, water8, water9 = st.columns(3)

        with water7:
            st.subheader("เบรอว์นี่")
            st.image("https://i.pinimg.com/564x/3f/fd/fc/3ffdfce3e0771841e02353547aba1c3b.jpg")
            st.write("10 บาท")

        with water8:
            st.header("มัฟฟินช็อค")
            st.image("https://i.pinimg.com/564x/50/61/8d/50618d0f6f4ff9e201859fa3151b116f.jpg")
            st.write('30 บาท')

        with water9:
            st.header("โดนัท")
            st.image("https://i.pinimg.com/564x/2c/d0/49/2cd049076dfd41d18476d7678070868d.jpg")
            st.write('129 บาท')

        water10 , water11 , water12 = st.columns(3)

        with water10:
            st.subheader("ทาร์ตสายรุ้ง")
            st.image("https://i.pinimg.com/564x/39/c1/f7/39c1f76fa73924aa7822d10e69d76a33.jpg")
            st.write("129 บาท")

        with water11:
            st.header("เค้กหมีช๊อคโกแลต")
            st.image("https://i.pinimg.com/564x/35/9c/91/359c91cc584c61895fe847af7d8fdff1.jpg")
            st.write('69 บาท')

        with water12:
            st.header("วาฟเฟิล")
            st.image("https://i.pinimg.com/236x/f1/1f/97/f11f976b0a79142bdd6e05728fa43eba.jpg")
            st.write('99 บาท')


with tab5:
    import streamlit as st
    import random

    # รายการเมนูน้ำ
    menu_drinks = [
        {"name": "ชาไทย (Thai Tea)", "image": "https://i.pinimg.com/564x/fd/be/17/fdbe1703e279924625d164a7f7e2643f.jpg"},
        {"name": "ชามะลิ (Jasmine tea)", "image": "https://i.pinimg.com/564x/82/20/6f/82206f450e59364fa7be7bed4606d0c4.jpg"},
        {"name": "ชาดำ (Black Tea)", "image": "https://i.pinimg.com/564x/06/6c/c8/066cc8984d807bf4b9fbc9d5bf6ae952.jpg"},
        {"name": "โกโก้ (Cocoa)", "image": "https://i.pinimg.com/564x/bc/72/e4/bc72e425fe957e6c481f1479ea4e2c8b.jpg"},
        {"name": "น้ำมะพร้าว (Coconut Water)", "image": "https://i.pinimg.com/564x/33/58/db/3358db9d6ba60a421fce93677ebb6460.jpg"},
        {"name": "น้ำแอปเปิ้ล (Apple Juice)", "image": "https://i.pinimg.com/564x/db/bd/72/dbbd726d3ecafa00ec1fdad8baf1d99b.jpg"},
        {"name": "น้ำส้ม (Orange Juice)", "image": "https://i.pinimg.com/564x/36/82/4e/36824eaf7777ee61865a43ad9646c4e1.jpg"},
        {"name": "น้ำเปล่า (Water)", "image": "https://i.pinimg.com/564x/64/b3/65/64b365d7c4b41f5a7d1ca71094b9297e.jpg"},
        {"name": "นมสด (Milk)", "image": "https://i.pinimg.com/564x/02/4f/9d/024f9d3b6a7ddd0eaddc758a21bbaf56.jpg"},
        {"name": "ชาเย็นไข่มุก (Iced Bubble Tea)", "image": "https://i.pinimg.com/564x/5e/bd/27/5ebd27adc0f326cfd0bd2bb1b5b99b29.jpg"},
        {"name": "ชาเขียว (Green tea)", "image": "https://i.pinimg.com/736x/32/3b/33/323b333b6edc8a1d811e45dc7231a1e9.jpg"},
        {"name": "ชาชมพู (Roselle Tea)", "image": "https://i.pinimg.com/564x/d2/24/91/d22491eb64c8e3de35583a5d81e930d4.jpg"},
        {"name": "ชาไทย (Thai Tea)", "image": "https://i.pinimg.com/564x/fd/be/17/fdbe1703e279924625d164a7f7e2643f.jpg"}
    ]

    # รายการเมนูขนมหวาน
    menu_desserts = [
        {"name": "เค้กช็อกโกแลต", "image": "https://i.pinimg.com/736x/69/66/fc/6966fce4b3153c05b176e21fe37d9b4a.jpg"},
        {"name": "ไอศกรีม", "image": "https://i.pinimg.com/564x/6d/e2/ce/6de2ce991c66b6136eb72243f12c449e.jpg"},
        {"name": "บราวนี่", "image": "https://i.pinimg.com/564x/68/8a/4d/688a4d8dd8ed6f08d51728c2257ffb19.jpg"},
        {"name": "เค้กสตรอเบอร์รี่", "image": "https://i.pinimg.com/564x/9d/cf/c1/9dcfc133a1a95384d456c6346837780a.jpg"},
        {"name": "พายแอปเปิ้ล", "image": "https://i.pinimg.com/564x/dd/de/26/ddde26a3252888d4f505fcf2b63751f2.jpg"},
        {"name": "คุโรบิสครีม", "image": "https://i.pinimg.com/564x/e7/f6/a6/e7f6a66343620a1d816255e90f5e78e6.jpg"},
        {"name": "เบรอว์นี่", "image": "https://i.pinimg.com/564x/3f/fd/fc/3ffdfce3e0771841e02353547aba1c3b.jpg"},
        {"name": "มัฟฟินช็อค", "image": "https://i.pinimg.com/564x/50/61/8d/50618d0f6f4ff9e201859fa3151b116f.jpg"},
        {"name": "โดนัท", "image": "https://i.pinimg.com/564x/2c/d0/49/2cd049076dfd41d18476d7678070868d.jpg"},
        {"name": "ทาร์ตสายรุ้ง", "image": "https://i.pinimg.com/564x/39/c1/f7/39c1f76fa73924aa7822d10e69d76a33.jpg"},
        {"name": "เค้กหมีช๊อคโกแลต", "image": "https://i.pinimg.com/564x/35/9c/91/359c91cc584c61895fe847af7d8fdff1.jpg"},
        {"name": "วาฟเฟิล", "image": "https://i.pinimg.com/236x/f1/1f/97/f11f976b0a79142bdd6e05728fa43eba.jpg"}
    ]

    # รายการเมนูกาแฟ
    menu_coffee = [
        {"name": "Espresso", "image": "https://i.pinimg.com/564x/5c/f7/9c/5cf79ce28f2ebd3f97ffff1fadd0d6f9.jpg"},
        {"name": "Americano", "image": "https://i.pinimg.com/564x/93/50/8d/93508dfce47fd1d677be051d6527a0b4.jpg"},
        {"name": "Latte", "image": "https://i.pinimg.com/564x/2b/da/de/2bdadea984bfafb8c65c52f00bcc7ef7.jpg"},
        {"name": "Cappuccino", "image": "https://i.pinimg.com/564x/2d/d4/cf/2dd4cfb175eb4cb2e17bf5bc0c8b59cc.jpg"},
        {"name": "Mocha", "image": "https://i.pinimg.com/564x/ec/65/9e/ec659ee19d12b2890931d575f6d13e1a.jpg"},
        {"name": "Macchiato", "image": "https://i.pinimg.com/564x/97/ec/f7/97ecf715edbaf993f2c65c4e6123f4df.jpg"},
        {"name": "Affogato", "image": "https://i.pinimg.com/564x/79/02/86/7902868d58cb28083caf50306bc2af1f.jpg"},
        {"name": "Ristretto", "image": "https://i.pinimg.com/564x/30/e4/fa/30e4fa735cb021afb7bbb4cba939f499.jpg"},
        {"name": "Iced Brew", "image": "https://i.pinimg.com/564x/2a/25/1e/2a251ede65e506f664936d7dc270642b.jpg"},
    ]

    # ปุ่มสำหรับสุ่มเมนู
    if st.button("สุ่มเมนูน้ำ"):
        random_drink = random.choice(menu_drinks)
        st.write("เมนูน้ำที่สุ่มได้:", random_drink["name"])
        st.image(random_drink["image"], caption=random_drink["name"], use_column_width=True)

    if st.button("สุ่มเมนูขนมหวาน"):
        random_dessert = random.choice(menu_desserts)
        st.write("เมนูขนมหวานที่สุ่มได้:", random_dessert["name"])
        st.image(random_dessert["image"], caption=random_dessert["name"], use_column_width=True)

    if st.button("สุ่มเมนูกาแฟ"):
        random_coffee = random.choice(menu_coffee)
        st.write("เมนูกาแฟที่สุ่มได้:", random_coffee["name"])
        st.image(random_coffee["image"], caption=random_coffee["name"], use_column_width=True)

with tab6:
    # ข้อมูลของร้านคาเฟ่รอบมหาลัย
    cafe_data = pd.DataFrame({
        'เมนู': ['ชาไทย', 'โกโก้', 'เค้กหมีช๊อคโกแลต'],
        'รีวิวจากลูกค้า': ['ชาไทยคือดีย์ต่อใจ', 'โกโก้เข้ม อร่อยดี', 'อร่อยมากแม่ ไม่ลองไม่ได้และ'],
        'ให้คะแนน': ['10/10', '5/10', '8/10']
    })

    # แสดงข้อมูลในตาราง
    st.title('รีวิวคาเฟ่')
    st.table(cafe_data)

    # เพิ่มฟอร์มสำหรับเพิ่มข้อมูลร้านคาเฟ่
    st.subheader('เพิ่มเมนู')
    new_cafe_name = st.text_input('ชื่อเมนู:')
    new_cafe_location = st.text_input('รีวิว:')
    new_cafe_phone = st.text_input('ให้คะเเนน:')

    if st.button('เพิ่มร้า'):
        # เพิ่มข้อมูลใหม่ลงในตาราง
        new_cafe_data = pd.DataFrame({
    'เมนู': [new_cafe_name],  # แก้เป็น 'เมนู' แทน 'ชื่อเมนู '
    'รีวิวจากลูกค้า': [new_cafe_location],  # แก้เป็น 'รีวิวจากลูกค้า' แทน 'รีวิว '
    'ให้คะแนน': [new_cafe_phone]  # แก้เป็น 'ให้คะแนน' แทน 'ให้คะเเนน '
})

        cafe_data = pd.concat([cafe_data, new_cafe_data], ignore_index=True)
        st.success('เพิ่มร้านคาเฟ่ใหม่เรียบร้อยแล้ว!')

    # แสดงสถานะของการเพิ่มร้านคาเฟ่
    st.write(cafe_data)


with tab7:
    def main():
        st.title("ติดต่อเรา")
        st.write("หากคุณมีคำถามหรือข้อสงสัยเกี่ยวกับเว็บไซต์ของเรา โปรดกรอกแบบฟอร์มด้านล่าง เราจะติดต่อกลับโดยเร็วที่สุด!")

        # ส่วนของแบบฟอร์มติดต่อ
        name = st.text_input("ชื่อของคุณ")
        email = st.text_input("อีเมลของคุณ")
        message = st.text_area("ข้อความ")

        if st.button("ส่งข้อความ"):
            # ส่วนประมวลผลข้อความที่ส่ง
            # อาจจะเก็บข้อมูลลงในฐานข้อมูลหรือส่งอีเมลไปยังผู้ดูแลเว็บไซต์
            st.success("ข้อความถูกส่งเรียบร้อยแล้ว!")

    if __name__ == "__main__":
        main()

