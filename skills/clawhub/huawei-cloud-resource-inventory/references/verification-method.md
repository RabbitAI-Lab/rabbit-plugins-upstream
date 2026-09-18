# 验证方法

## 验证步骤

### 1. 依赖验证

```bash
pip install -r requirements.txt
python3 -c "from huaweicloudsdkecs.v2.ecs_client import EcsClient; print('ECS SDK OK')"
python3 -c "from huaweicloudsdkvpc.v3.vpc_client import VpcClient; print('VPC SDK OK')"
```

### 2. 凭据验证

```bash
python3 -c "
import os
ak = os.getenv('HUAWEICLOUD_SDK_AK') or os.getenv('OBS_ACCESS_KEY') or os.getenv('HW_ACCESS_KEY')
sk = os.getenv('HUAWEICLOUD_SDK_SK') or os.getenv('OBS_SECRET_KEY') or os.getenv('HW_SECRET_KEY')
if ak and sk:
    print('Credentials OK')
else:
    print('ERROR: Credentials not found')
    exit(1)
"
```

### 3. 功能验证

```bash
# 测试 --help
python3 scripts/resource_inventory.py --help

# 测试 --capability-list
python3 scripts/resource_inventory.py --capability-list

# 测试单 region 查询
python3 scripts/resource_inventory.py --region cn-north-4

# 测试 JSON 输出
python3 scripts/resource_inventory.py --region cn-north-4 --format json

# 测试资源类型过滤
python3 scripts/resource_inventory.py --resource-type ecs,vpc
```

### 4. 输出验证

- 表格输出应包含至少一个资源类型的表头和数据行
- 关联字段（如 vpc_id, subnet_id, attached_to）应有值或显示 "-"
- 查询错误应在 "Query Errors / Warnings" 段落中列出
- Summary 应显示各资源类型的总数

### 5. 关联关系验证

- ECS 表中 vpc_id 应与 VPC 表中的 id 匹配
- EIP 表中 associated_server 应与 ECS 表中的 id 匹配
- EVS 表中 attached_to 应与 ECS 表中的 id 匹配
- Subnet 表中 vpc_id 应与 VPC 表中的 id 匹配
