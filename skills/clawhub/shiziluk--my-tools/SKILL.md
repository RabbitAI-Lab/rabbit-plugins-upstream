---
name: my-tools
description: 我的自定义工具集，提供获取当前时间和计算数学表达式的功能
---

# my_tools 技能

这个技能提供以下功能，请在用户提出相关请求时调用：

## get_current_time
当用户询问"现在几点"、"当前时间"、"日期"等时，使用 `exec` 工具执行以下命令获取当前时间：

```powershell
Get-Date -Format "yyyy-MM-dd HH:mm:ss"
```

## calculator
当用户要求计算数学表达式时，使用 `exec` 工具执行以下命令进行计算：

```powershell
py -c "print(eval('EXPRESSION'))"
```

将 EXPRESSION 替换为用户提供的表达式。
