# Python ATM 银行存取款系统

Python 入门学习项目，模拟银行 ATM 的查询余额、存款、取款和退出流程。项目保留命令行交互体验，同时把账户业务逻辑抽成 `ATMAccount` 类，方便测试和后续扩展。

## 功能
- 查询余额
- 存款操作
- 取款操作（含余额不足检查）
- 输入校验（负数、非数字拦截）
- 使用 `Decimal` 处理金额，避免浮点数精度问题
- 单元测试覆盖存款、取款、余额不足、输入解析和金额格式化

## 运行

```bash
python atm.py
```

## 测试

```bash
python -m unittest discover -s tests
```

## 代码结构

```text
atm.py
tests/
  test_atm.py
```

核心逻辑：

- `ATMAccount.deposit()`：存款并返回最新余额
- `ATMAccount.withdraw()`：取款，余额不足时抛出 `ATMError`
- `parse_amount()`：解析用户输入金额
- `format_money()`：格式化金额显示
