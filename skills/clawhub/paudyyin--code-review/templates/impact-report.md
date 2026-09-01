## 变更影响面分析

**分析时间**: {{timestamp}}
**变更文件数**: {{changed_count}}
**影响范围**: {{summary}}

### 直接影响（{{direct_count}}个文件）
{% for item in direct %}
- `{{item.file}}` ← import了 `{{item.imports}}`
{% endfor %}

### 间接影响（{{indirect_count}}个文件）
{% for item in indirect %}
- `{{item.file}}` ← import了 `{{item.via}}`（via `{{item.via}}`）
{% endfor %}

### 潜在影响（{{potential_count}}个文件）
{% for item in potential %}
- `{{item.file}}` ← {{item.reason}}
{% endfor %}

**风险评估**: {{risk_level}}
{% if risk_level == 'high' %}
⚠️ 建议重点审查间接影响文件的接口兼容性
{% elif risk_level == 'medium' %}
建议审查直接影响文件的接口兼容性
{% else %}
变更影响范围可控
{% endif %}
