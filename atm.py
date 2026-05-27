# 银行存取款系统案例

# 初始化账户余额（单位：元）
money = 1000000  # 100万
name = input("请输入您的姓名")

def display_menu():
    """显示功能菜单"""
    print("\n" + "=" * 30)
    print(f"      尊敬的{name}欢迎使用银行存取款系统")
    print("=" * 30)
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出系统")
    print("=" * 30)

def check_balance():
    """查询余额"""
    global money #使用全局变量
    print(f"\n当前账户余额：{money:,} 元")
    print(f"（共 {money // 10000} 万元）")

def deposit():
    """存款操作"""
    global money

    # 获取存款金额
    try:
        amount = float(input("请输入存款金额（元）："))
    except ValueError:
        print("错误：请输入有效的数字！")
        return # 退出函数

    # 检查存款金额是否有效
    if amount <= 0:
        print("错误：存款金额必须大于0！")
        return

    # 执行存款操作
    money += amount
    print(f"存款成功！存入 {amount:,.2f} 元")
    print(f"当前余额：{money:,.2f} 元")

def withdraw():
    """取款操作"""
    global money

    # 获取取款金额
    try:
        amount = float(input("请输入取款金额（元）："))
    except ValueError:
        print("错误：请输入有效的数字！")
        return

    # 检查取款金额是否有效
    if amount <= 0:
        print("错误：取款金额必须大于0！")
        return

    # 检查余额是否充足
    if amount > money:
        print(f"错误：余额不足！当前余额：{money:,.2f} 元")
        return

    # 执行取款操作
    money -= amount
    print(f"取款成功！取出 {amount:,.2f} 元")
    print(f"当前余额：{money:,.2f} 元")

def main():
    """主程序"""
    global money

    print("银行存取款系统已启动")
    print(f"初始余额：{money:,} 元")

    while True:
        # 显示菜单
        display_menu()

        # 获取用户选择
        choice = input("请选择操作（1-4）：")

        # 根据用户选择执行相应操作
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("\n感谢使用银行存取款系统，再见！")
            print(f"最终余额：{money:,} 元")
            break
        else:
            print("错误：请输入1-4之间的数字！")

# 程序入口
if __name__ == "__main__":
    main()