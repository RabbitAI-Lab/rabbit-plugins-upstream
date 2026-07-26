# 数据处理详细规范

## 1. 字段识别

### 自动映射规则（模糊匹配，优先级从高到低）

```python
FIELD_PATTERNS = {
    'date': ['预订日期', '下单时间', '订单日期', '日期', 'date', 'order_date', 'created_at'],
    'amount': ['订单最终金额', '实收金额', '实付金额', '订单金额', '金额', 'amount', 'price', 'total'],
    'order_amount': ['订单金额', '原价', 'original_price'],
    'user_id': ['手机号', '用户ID', '会员号', 'user_id', 'phone', 'member_id', 'customer_id'],
    'item': ['场地', '商品', '服务', '项目', '品类', 'item', 'product', 'service', 'court'],
    'slot': ['预订时段', '时段', '时间段', 'slot', 'time_slot', 'hour'],
    'status': ['订单状态', '状态', 'status', 'order_status'],
    'discount': ['优惠金额', '折扣', 'discount', 'coupon'],
}

def detect_fields(df):
    mapping = {}
    for std_name, patterns in FIELD_PATTERNS.items():
        for col in df.columns:
            if any(p.lower() in col.lower() for p in patterns):
                mapping[std_name] = col
                break
    return mapping
```

### 必须字段处理
- `date`：缺失则报错，提示用户指定日期列
- `amount`：缺失则尝试用 `order_amount` 代替，仍缺则只统计场次不统计收入
- `user_id`：缺失则只做订单分析，跳过用户留存分析

---

## 2. 多行拆分（场馆/多项目场景）

### 触发条件
字段值包含 `;` 分隔符，如：
- `场地`: `场地01;场地03`
- `时段`: `08:00~09:00;09:00~10:00`

### 拆分逻辑

```python
from itertools import product

def expand_row(row, item_col, slot_col):
    items = str(row[item_col]).split(';') if item_col else ['unknown']
    slots = str(row[slot_col]).split(';') if slot_col else ['unknown']
    
    # 判断展开模式
    if len(items) == 1 or len(slots) == 1:
        combos = list(product(items, slots))
    else:
        # 先尝试配对（1:1映射）
        n = max(len(items), len(slots))
        paired = [(items[min(i,len(items)-1)], slots[min(i,len(slots)-1)]) for i in range(n)]
        # 验证配对总价是否接近原始金额
        # 如不匹配则改用笛卡尔积
        combos = paired  # 默认配对
    
    return combos

def split_amount(total, std_prices, total_std):
    """按标准单价比例分摊金额"""
    if total_std == 0:
        return [total / len(std_prices)] * len(std_prices)
    return [total * p / total_std for p in std_prices]
```

---

## 3. 核心指标计算规范

### 3.1 时间处理

```python
df['date'] = pd.to_datetime(df['date'], errors='coerce', infer_datetime_format=True)
df['month'] = df['date'].dt.to_period('M').astype(str)
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday  # 0=周一, 6=周日
df['is_weekend'] = df['weekday'] >= 5
df['hour'] = df['date'].dt.hour  # 如果时段是时间戳
# 如果时段是字符串如"08:00~09:00"，提取起始小时：
df['hour'] = df['slot'].str.extract(r'(\d+):').astype(float)
```

### 3.2 月度日均指标（推荐口径，排除天数差异）

```python
def calc_monthly(df, exclude_dates=None):
    """
    exclude_dates: list of (month, day_start, day_end) tuples for lockout periods
    e.g., [('2026-02', 15, 22)] for CNY lockout
    """
    if exclude_dates:
        for month, d1, d2 in exclude_dates:
            mask = (df['month'] == month) & df['day'].between(d1, d2)
            df = df[~mask]
    
    monthly = df.groupby('month').agg(
        total_orders=('amount', 'count'),
        total_rev=('amount', 'sum'),
        active_users=('user_id', 'nunique'),
        op_days=('date', lambda x: x.dt.date.nunique())
    ).reset_index()
    
    monthly['daily_orders'] = (monthly['total_orders'] / monthly['op_days']).round(1)
    monthly['daily_rev'] = (monthly['total_rev'] / monthly['op_days']).round(0)
    return monthly
```

### 3.3 新老用户判断

```python
def classify_users(df, old_pool_months=None, old_pool_users=None):
    """
    方式A: 指定月份作为老用户基准期（前N个月已订过=老用户）
    方式B: 直接提供老用户集合
    """
    first_order = df.groupby('user_id')['date'].min().reset_index()
    first_order.columns = ['user_id', 'first_order_date']
    first_order['first_month'] = first_order['first_order_date'].dt.to_period('M').astype(str)
    
    if old_pool_months:
        old_users = set(first_order[first_order['first_month'].isin(old_pool_months)]['user_id'])
    elif old_pool_users:
        old_users = set(old_pool_users)
    else:
        # 默认：数据集中最早出现的月份用户为老用户基准
        earliest_months = sorted(first_order['first_month'].unique())[:3]
        old_users = set(first_order[first_order['first_month'].isin(earliest_months)]['user_id'])
    
    return old_users, first_order
```

### 3.4 新用户次月留存

```python
def calc_retention(df, first_order_df, old_pool):
    months = sorted(df['month'].unique())
    retention = []
    
    for i, mo in enumerate(months[:-1]):
        next_mo = months[i+1]
        # 本月首次订单的新用户（不在老用户池中）
        new_users = set(
            first_order_df[
                (first_order_df['first_month'] == mo) &
                (~first_order_df['user_id'].isin(old_pool))
            ]['user_id']
        )
        if not new_users:
            continue
        next_month_users = set(df[df['month'] == next_mo]['user_id'])
        retained = new_users & next_month_users
        retention.append({
            'period': f"{mo}→{next_mo}",
            'new_users': len(new_users),
            'retained': len(retained),
            'rate': round(len(retained) / len(new_users) * 100, 1)
        })
    return retention
```

### 3.5 逐小时日均（整月数据）

```python
def calc_hourly(df, exclude_dates=None):
    if exclude_dates:
        for month, d1, d2 in exclude_dates:
            mask = (df['month'] == month) & df['day'].between(d1, d2)
            df = df[~mask]
    
    result = {}
    for mo in df['month'].unique():
        m = df[df['month'] == mo]
        op_days = m['date'].dt.date.nunique()
        hourly = m.groupby('hour').size() / op_days
        result[mo] = {int(h): round(v, 2) for h, v in hourly.items()}
    return result
```

### 3.6 频次分布

```python
def freq_distribution(df_period, user_col='user_id'):
    uf = df_period.groupby(user_col).size()
    return {
        '1次': int((uf == 1).sum()),
        '2次': int((uf == 2).sum()),
        '3-5次': int(((uf >= 3) & (uf <= 5)).sum()),
        '5+次': int((uf > 5).sum())
    }
```

---

## 4. 等长时间段对比（阶段环比）

```python
def get_comparable_periods(df, period_days=15):
    """
    自动选取最近若干个月，各取前N天做等长对比
    支持春节等特殊期补全
    """
    months = sorted(df['month'].unique())[-4:]  # 最近4个月
    periods = []
    
    for mo in months:
        m_data = df[df['month'] == mo]
        m_data = m_data[m_data['day'] <= period_days]
        periods.append({
            'label': mo,
            'data': m_data,
            'days': period_days
        })
    return periods
```

### 特殊期补全（如春节锁场）

```python
def fill_missing_period(real_data, ref_data, fill_dates, weekday_map):
    """
    real_data: 实际有数据的部分
    ref_data: 同月非特殊期数据
    fill_dates: 需要补全的日期列表
    weekday_map: {weekday: avg_value} 按星期的平均值
    """
    fill_values = {}
    for d in fill_dates:
        dow = d.weekday()
        fill_values[d] = weekday_map.get(dow, weekday_map.get('avg', 0))
    return fill_values
```

---

## 5. 数据质量检查

处理前自动检查：
```python
def data_quality_check(df, field_map):
    issues = []
    
    # 1. 缺失值
    for std, col in field_map.items():
        null_pct = df[col].isna().mean()
        if null_pct > 0.05:
            issues.append(f"字段 {col} 缺失率 {null_pct:.1%}")
    
    # 2. 日期范围
    date_col = field_map.get('date')
    if date_col:
        date_range = df[date_col].agg(['min', 'max'])
        issues.append(f"数据范围：{date_range['min']:%Y-%m-%d} 至 {date_range['max']:%Y-%m-%d}")
    
    # 3. 金额异常
    amt_col = field_map.get('amount')
    if amt_col:
        neg = (df[amt_col] < 0).sum()
        if neg > 0:
            issues.append(f"存在 {neg} 条负金额记录")
    
    return issues
```
