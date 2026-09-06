# 验方法

## 前置条件

1. 确保已安装依赖：`pip install huaweicloudsdk-cce huaweicloudsdk-core`
2. 确保已配置华为云 AK/SK 环境变量

## 验证步骤

### 1. 查询集群列表

```bash
python3 scripts/huawei-cloud-cce-list.py
```

预期输出：
- 如果账号下存在 CCE 集群，输出表格格式的集群列表（名称、状态、集群版本、平台版本）
- 如果账号下没有 CCE 集群，输出"未找到任何 CCE 集群"

### 2. 指定区域查询

```bash
python3 scripts/huawei-cloud-cce-list.py --region cn-north-1
```

### 3. 参数缺失测试

```bash
unset HUAWEICLOUD_SDK_AK
unset HUAWEICLOUD_SDK_SK
python3 scripts/huawei-cloud-cce-list.py
```

预期输出：错误提示"未找到 AK/SK 环境变量"，退出码 3

### 4. 帮助信息

```bash
python3 scripts/huawei-cloud-cce-list.py --help
```

## 验证结果记录

| 测试项 | 预期结果 | 实际结果 |
|--------|---------|---------|
| 查询集群列表 | 表格输出或"未找到" | |
| 指定区域 | 正常输出 | |
| AK/SK缺失 | 退出码3 | |
| --help | 显示帮助信息 | |