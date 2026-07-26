# Commit 规范详解

## 基本格式

```
<type>(module): <description>
```

**格式说明**:
- `type`: 必填,提交类型(feat/fix/test/docs/refactor/chore/revert)
- `(module)`: 必填,模块名,必须用圆括号包裹
- `description`: 必填,提交描述,英文、动词开头、小写

---

## Type 详解

### 1. fix - 修复缺陷

```
fix(module): <description>
```

**示例**:
```bash
fix(auth): resolve null pointer exception
fix(parser): fix memory leak in cache module
```

---

### 2. feat - 新功能/需求

```
feat(module): <description>
```

**示例**:
```bash
feat(auth): add user login module
feat(skills): add k8s troubleshoot skill
```

**注意**:模块名必须用 `()` 包裹

---

### 3. test - 测试改动

```
test(module): <description>
```

**示例**:
```bash
test(auth): add unit tests for login
test(auth): add integration tests
```

---

### 4. docs - 文档修改

```
docs(module): <description>
```

**示例**:
```bash
docs(api): update authentication documentation
docs(readme): add installation guide
```

---

### 5. revert - 回滚提交

```
revert(module): <description>
```

**示例**:
```bash
revert(auth): revert login module changes
```

---

### 6. refactor - 代码重构

```
refactor(module): <description>
```

**示例**:
```bash
refactor(utils): extract common helper functions
refactor(auth): optimize login flow
```

---

### 7. chore - 其他修改

```
chore(module): <description>
```

**示例**:
```bash
chore(deps): update npm dependencies
chore(build): optimize webpack config
```

---

### 8. 多次提交

用于多次提交对应一个需求,前面用 `feat`,最后一次也用 `feat`

```
feat(module): <description>
```

**示例**:
```bash
# 第一次提交
feat(auth): implement login validation

# 第二次提交
feat(auth): add session management

# 最后一次提交
feat(auth): complete user authentication module
```
