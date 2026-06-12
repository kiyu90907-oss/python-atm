from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


class ATMError(ValueError):
    """ATM 业务异常。"""


@dataclass
class ATMAccount:
    owner: str
    balance: Decimal = Decimal("1000000")

    def deposit(self, amount: Decimal) -> Decimal:
        amount = validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount: Decimal) -> Decimal:
        amount = validate_amount(amount)
        if amount > self.balance:
            raise ATMError(f"余额不足，当前余额：{format_money(self.balance)} 元")
        self.balance -= amount
        return self.balance


def parse_amount(raw_value: str) -> Decimal:
    """把用户输入转换为 Decimal 金额。"""
    try:
        return Decimal(raw_value.strip())
    except (InvalidOperation, AttributeError):
        raise ATMError("请输入有效的数字") from None


def validate_amount(amount: Decimal) -> Decimal:
    if amount <= 0:
        raise ATMError("金额必须大于 0")
    return amount.quantize(Decimal("0.01"))


def format_money(amount: Decimal) -> str:
    return f"{amount:,.2f}"


def display_menu(account: ATMAccount) -> None:
    print("\n" + "=" * 30)
    print(f"      尊敬的 {account.owner}，欢迎使用银行 ATM 系统")
    print("=" * 30)
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出系统")
    print("=" * 30)


def check_balance(account: ATMAccount) -> None:
    print(f"\n当前账户余额：{format_money(account.balance)} 元")
    print(f"约 {account.balance // Decimal('10000')} 万元")


def prompt_amount(message: str) -> Decimal | None:
    try:
        return parse_amount(input(message))
    except ATMError as exc:
        print(f"错误：{exc}！")
        return None


def deposit(account: ATMAccount) -> None:
    amount = prompt_amount("请输入存款金额（元）：")
    if amount is None:
        return

    try:
        account.deposit(amount)
    except ATMError as exc:
        print(f"错误：{exc}！")
        return

    print(f"存款成功！存入 {format_money(amount)} 元")
    print(f"当前余额：{format_money(account.balance)} 元")


def withdraw(account: ATMAccount) -> None:
    amount = prompt_amount("请输入取款金额（元）：")
    if amount is None:
        return

    try:
        account.withdraw(amount)
    except ATMError as exc:
        print(f"错误：{exc}！")
        return

    print(f"取款成功！取出 {format_money(amount)} 元")
    print(f"当前余额：{format_money(account.balance)} 元")


def main() -> None:
    name = input("请输入您的姓名：").strip() or "用户"
    account = ATMAccount(owner=name)

    print("银行 ATM 系统已启动")
    print(f"初始余额：{format_money(account.balance)} 元")

    while True:
        display_menu(account)
        choice = input("请选择操作（1-4）：").strip()

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            print("\n感谢使用银行 ATM 系统，再见！")
            print(f"最终余额：{format_money(account.balance)} 元")
            break
        else:
            print("错误：请输入 1-4 之间的数字！")


if __name__ == "__main__":
    main()
