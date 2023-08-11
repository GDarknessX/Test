import streamlit as st
st.title("健康小问题")

def main():


    # 问题和选项
    option_aa = "沉脉"
    option_bb = "迟脉"
    option_cc = "浮脉"
    option_dd = "实脉"
    option_ee = "数脉"
    option_ff = "虚脉"
    question_a = "你比较胖/瘦？"    # Chenmai
    option_a_a = "胖"
    option_a_b = "瘦"
    question_b = "你是否最近感觉到困乏疲惫？"
    option_b_a = "是"
    option_b_b = "否"
 
    question_c = "你最近吃饭的胃口怎么样？"
    option_c_a = "好"
    option_c_b = "坏"
 
    question_d = "你长期从事体力劳动或高强度运动吗？"    #Chimai
    option_d_a = "是"
    option_d_b = "否"
 
    question_e = "你最近排便顺畅吗？"   
    option_e_a = "是"
    option_e_b = "否"
 
    question_f = "你常居住在高海拔区？"
    option_f_a = "是"
    option_f_b = "否"
 
    question_g = "你最近有吹冷风着凉的经历吗？"
    option_g_a = "是"
    option_g_b = "否"
 
    question_h = "你感到冷/热吗？"    #Fumai
    option_h_a = "冷"
    option_h_b = "热"
 
    question_i= "你比较胖/瘦？"
    option_i_a = "胖"
    option_i_b = "瘦"
 
    question_j = "你是否有长期的疾病史？"
    option_j_a = "是"
    option_j_b = "否"
 
    question_k = "你最近是否发烧或者感冒过？" #Shimai
    option_k_a = "是"
    option_k_b = "否"
 
    question_l = "你喜欢喝酒吗？"
    option_l_a = "是"
    option_l_b = "否"
 
    question_m = "你经常熬夜吗？"
    option_m_a = "是"
    option_m_b = "否"
 
    question_n = "你最近总是发脾气吗？"
    option_n_a = "是"
    option_n_b = "否"
 
    question_o = "你感觉到热吗？"    #Shumai
    option_o_a = "是"
    option_o_b = "否"
 
    question_p = "你晚上睡觉流汗吗？"
    option_p_a = "是"
    option_p_b = "否"
 
    question_q = "你常常感觉气短心跳加速吗？"
    option_q_a = "是"
    option_q_b = "否"
 
    question_r = "你最近有消化不良吗？" #Xumai
    option_r_a = "是"
    option_r_b = "否"
 
    question_s = "你贫血吗？"
    option_s_a = "是"
    option_s_b = "否"
    question_t = "你瘦吗？"
    option_t_a = "是"
    option_t_b = "否"
    
    if st.session_state.question == "initial":
        st.write("请选择一个脉象：")
        if st.button("沉脉"):
            st.session_state.question = "a"
            st.experimental_rerun()
        elif st.button("迟脉"):
            st.session_state.question = "d"
            st.experimental_rerun()
        elif st.button("浮脉"):
            st.session_state.question = "i"
            st.experimental_rerun()
        elif st.button("实脉"):
            st.session_state.question = "k"
            st.experimental_rerun()
        elif st.button("数脉"):
            st.session_state.question = "o"
            st.experimental_rerun()
        elif st.button("虚脉"):
            st.session_state.question = "r"
            st.experimental_rerun()
    # 沉脉
    if st.session_state.question == "a":
        st.session_state.x = 1
        st.write(question_a)
        # 显示选项按钮
        if st.button(option_a_a):
            st.write(f"您选择了 {option_a_a}。")
            st.session_state.question = "b"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_a_b):
            st.write(f"您选择了 {option_a_b}。")
            st.session_state.question = "b"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "b":
        st.write(question_b)
        # 显示选项按钮
        if st.button(option_b_a):
            st.write(f"您选择了 {option_b_a}。")
            st.session_state.question = "c"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_b_b):
            st.write(f"您选择了 {option_b_b}。")
            st.session_state.question = "c"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
            
    elif st.session_state.question == "c":
        st.write(question_c)
        # 显示选项按钮
        if st.button(option_c_a):
            st.write(f"您选择了 {option_c_a}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_c_b):
            st.write(f"您选择了 {option_b_b}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
#迟脉
    if st.session_state.question == "d":
        st.session_state.x=2
        st.write(question_d)
        # 显示选项按钮
        if st.button(option_d_a):
            st.write(f"您选择了 {option_d_a}。")
            st.session_state.question = "e"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_d_b):
            st.write(f"您选择了 {option_d_b}。")
            st.session_state.question = "e"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "e":
        st.write(question_e)
        # 显示选项按钮
        if st.button(option_e_a):
            st.write(f"您选择了 {option_e_a}。")
            st.session_state.question = "g"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_e_b):
            st.write(f"您选择了 {option_e_b}。")
            st.session_state.question = "g"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
            
    elif st.session_state.question == "g":
        st.write(question_g)
        # 显示选项按钮
        if st.button(option_g_a):
            st.write(f"您选择了 {option_g_a}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_g_b):
            st.write(f"您选择了 {option_g_b}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
#浮脉
    if st.session_state.question == "i":
        st.session_state.x = 7
        st.write(question_i)
        # 显示选项按钮
        if st.button(option_i_a):
            st.write(f"您选择了 {option_i_a}。")
            st.session_state.question = "h"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_i_b):
            st.write(f"您选择了 {option_i_b}。")
            st.session_state.question = "h"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "h":
        st.write(question_h)
        # 显示选项按钮
        if st.button(option_h_a):
            st.write(f"您选择了 {option_h_a}。")
            st.session_state.question = "j"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_h_b):
            st.write(f"您选择了 {option_h_b}。")
            st.session_state.question = "j"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
            
    elif st.session_state.question == "j":
        st.write(question_j)
        # 显示选项按钮
        if st.button(option_j_a):
            st.write(f"您选择了 {option_j_a}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_j_b):
            st.write(f"您选择了 {option_j_b}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
#实脉
    if st.session_state.question == "k":
        st.session_state.x=4
        st.write(question_k)
        # 显示选项按钮
        if st.button(option_k_a):
            st.write(f"您选择了 {option_k_a}。")
            st.session_state.question = "l"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_k_b):
            st.write(f"您选择了 {option_k_b}。")
            st.session_state.question = "l"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "l":
        st.write(question_l)
        # 显示选项按钮
        if st.button(option_l_a):
            st.write(f"您选择了 {option_l_a}。")
            st.session_state.question = "m"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_l_b):
            st.write(f"您选择了 {option_l_b}。")
            st.session_state.question = "m"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
            
    elif st.session_state.question == "m":
        st.write(question_m)
        # 显示选项按钮
        if st.button(option_m_a):
            st.write(f"您选择了 {option_m_a}。")
            st.session_state.question = "n"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_m_b):
            st.write(f"您选择了 {option_m_b}。")
            st.session_state.question = "n"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "n":
        st.write(question_n)
        # 显示选项按钮
        if st.button(option_n_a):
            st.write(f"您选择了 {option_n_a}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_n_b):
            st.write(f"您选择了 {option_n_b}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
#数脉
    if st.session_state.question == "o":
        st.session_state.x =5
        st.write(question_o)
        # 显示选项按钮
        if st.button(option_o_a):
            st.write(f"您选择了 {option_o_a}。")
            st.session_state.question = "p"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_o_b):
            st.write(f"您选择了 {option_o_b}。")
            st.session_state.question = "p"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "p":
        st.write(question_p)
        # 显示选项按钮
        if st.button(option_p_a):
            st.write(f"您选择了 {option_p_a}。")
            st.session_state.question = "q"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_p_b):
            st.write(f"您选择了 {option_p_b}。")
            st.session_state.question = "q"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
            
    elif st.session_state.question == "q":
        st.write(question_q)
        # 显示选项按钮
        if st.button(option_q_a):
            st.write(f"您选择了 {option_q_a}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_q_b):
            st.write(f"您选择了 {option_q_b}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
#虚脉
    if st.session_state.question == "r":
        st.session_state.x=6
        st.write(question_r)
        # 显示选项按钮
        if st.button(option_r_a):
            st.write(f"您选择了 {option_r_a}。")
            st.session_state.question = "s"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_r_b):
            st.write(f"您选择了 {option_r_b}。")
            st.session_state.question = "s"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    elif st.session_state.question == "s":
        st.write(question_s)
        # 显示选项按钮
        if st.button(option_s_a):
            st.write(f"您选择了 {option_s_a}。")
            st.session_state.question = "t"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_s_b):
            st.write(f"您选择了 {option_s_b}。")
            st.session_state.question = "t"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
            
    elif st.session_state.question == "t":
        st.write(question_t)
        # 显示选项按钮
        if st.button(option_t_a):
            st.write(f"您选择了 {option_t_a}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+1
            st.experimental_rerun()
        elif st.button(option_t_b):
            st.write(f"您选择了 {option_t_b}。")
            st.session_state.question = "answer"
            st.session_state.x=st.session_state.x*10+2
            st.experimental_rerun()
    if st.session_state.question == "answer":
        if st.session_state.x == 7211 or st.session_state.x == 7212 or st.session_state.x == 7221 or st.session_state.x == 7222 or st.session_state.x == 1111 or st.session_state.x == 1112 or st.session_state.x == 1121 or st.session_state.x == 1122 or st.session_state.x == 2111 or st.session_state.x == 2112 or st.session_state.x == 2121 or st.session_state.x == 2122 or st.session_state.x == 42221 or st.session_state.x == 42222 or st.session_state.x == 5211 or st.session_state.x == 5212 or st.session_state.x == 5221 or st.session_state.x == 5222:
            st.text("正常")
        elif st.session_state.x == 7111 or st.session_state.x==7121 or st.session_state.x==41111or st.session_state.x==41112 or st.session_state.x==41121 or st.session_state.x==41122 or st.session_state.x==41211 or st.session_state.x==41212 or st.session_state.x==41221 or st.session_state.x==41222 or st.session_state.x==5111:
            st.text("就医")
        elif  st.session_state.x== 7112 :
            st.text("可能风寒侵袭→麻黄桂枝汤/姜汤")
        elif st.session_state.x==7122:
            st.text("风热、上火、有痰，外邪入侵→薄荷水/金银花茶/藿香正气水/罗汉果茶/绿豆汤")
        elif st.session_state.x==1211 or st.session_state.x==1212:
            st.text("阳气虚→乌鸡桂圆红枣汤/海参/牛羊肉、虾等高蛋白肉类/韭菜 ")
        elif st.session_state.x==1221:
            st.text("阳气被遏→附子理中汤加肉豆蔻、补骨脂、薏苡仁（伤寒论）/艾灸中脘")
        elif st.session_state.x==1222:
            st.text("阳气被遏→附子理中汤（伤寒论）/艾灸中脘")
        elif st.session_state.x ==2211:
            st.text("寒邪、风邪入体→葱白姜汤/胡椒汤面/麻黄汤（麻黄、桂枝、杏仁、甘草）-伤寒论")
        elif st.session_state.x==2212:
            st.text("阳气亏虚→人参/椒麻鸡/荔枝/龙眼/不喝冰水，每日泡脚")
        elif st.session_state.x==2221:
            st.text("寒邪、风邪入体→胡椒糙米瘦肉粥/玉米汁/青椒/充足睡眠")
        elif st.session_state.x==2222:
            st.text("阳气亏虚→附子理中汤（伤寒论）/六磨汤加红花、赤芍、当归")
        elif st.session_state.x==42211 or st.session_state.x==42212:
            st.text("孤阳外脱→肉桂、人参、山药、枸杞、当归煮汤")
        elif st.session_state.x==41111 or st.session_state.x==41112:
            st.text("阳亢→当归六黄汤/龙胆泻肝汤/归脾汤/核桃、酸枣仁、百合、茯苓做甜品、泡茶/桑葚/核桃")
        elif st.session_state.x==41121 or st.session_state.x==41122:
            st.text("阳亢→龙胆泻肝汤")
        elif st.session_state.x==6121:
            st.text("阳气不足→山药、鸡肉、生脉饮")
        elif st.session_state.x==6122:
            st.text("气虚→山药、鸡肉、生脉饮")
        elif st.session_state.x==6221:
            st.text("阳气不足→西洋参、党参、白扁豆、牛肉、山药")
        elif st.session_state.x==6222:
            st.text("正常→白扁豆、牛肉、山药")
        elif st.session_state.x==6112:
            st.text("血虚→十全大补汤 ")
        elif st.session_state.x==6111:
            st.text("血虚→红枣、红糖、四物汤")
        elif st.session_state.x==6211:
            st.text("血虚→羊肉汤加当归生姜")
        elif st.session_state.x==6212:
            st.text("血虚→红糖红枣姜汤/当归生姜茶")
        elif st.session_state.x==5112:
            st.text("热证→山药、菠菜、苦瓜、冬瓜、鸭肉、菊花、莲子、荸荠、山竹")
        elif st.session_state.x==5121:
            st.text("阳极阴竭→就医")
        elif st.session_state.x==5122:
            st.text("阳极阴竭→百合银耳雪梨羹、石斛、黑芝麻、桑葚、甲鱼、山药、菠菜、鸭肉、菊花、莲子、荸荠")
if __name__ == "__main__":
    if 'question' not in st.session_state:
        st.session_state.question = "initial"
    main()
