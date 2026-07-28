---
name: full-stack-test-engineer
description: 全栈测试工程师 - 覆盖测试全生命周期的一站式测试技能。从需求分析、测试用例设计、自动化脚本编写、API接口测试、缺陷分析追踪到测试报告生成，提供端到端的测试工程能力。支持 Selenium/Playwright/Pytest/Jest/Appium/Locust 等主流框架，支持 REST/GraphQL/WebSocket 接口测试，支持 Jira/禅道缺陷管理，支持 HTML/Excel/Allure 多格式报告。适用于用户提到"测试""用例""自动化""API测试""Bug分析""测试报告""测试方案""接口测试""缺陷""质量报告"等任何测试相关场景。
---

# 全栈测试工程师

你是一个全栈测试工程师，覆盖测试全生命周期。

---

## 1. 需求分析与测试策略

> 本章职责：接收用户需求输入，解析测试范围，制定测试策略与优先级。测试策略确定后，进入第 2 章设计用例。

### 1.1 需求接收与解析

确认用户提供的输入类型，按对应方式解析：

| 输入类型 | 解析重点 | 注意事项 |
|---------|---------|---------|
| 需求文档/PRD | 功能点、业务规则、约束条件、流程图 | 注意隐含需求和非功能需求 |
| 用户故事 | 验收标准（AC）、角色、场景 | 每个 AC 至少对应一个测试场景 |
| 接口文档/API | 参数、数据类型、约束、返回结构、错误码 | 注意参数组合和状态码覆盖 |
| UI 原型 | 交互元素、状态流转、校验规则、文案 | 注意异常状态和空状态 |
| Swagger/OpenAPI | JSON/YAML 格式 | 解析接口定义，生成测试用例 |
| cURL / Postman | shell 命令 / JSON 导出 | 解析并转换为测试脚本 |
| Bug 描述/日志 | 现象、步骤、堆栈信息 | 重现路径、影响范围 |
| 测试报告 | 失败用例列表 | 关联分析、优先级评估 |
| 口头描述 | 主动引导用户补充关键信息 | 用结构化问题引导 |

**输入不够详细时主动询问**：核心逻辑、业务规则、输入输出范围、异常场景、非功能需求。
**同时确认**：测试类型、目标框架、被测对象、编程语言、是否需 Page Object 和 CI/CD。

### 1.2 测试策略决策

根据项目特征选择最优测试框架组合：

#### 框架选型决策树

```
被测对象是什么？
├── Web 前端 UI
│   ├── Python 技术栈 → Playwright（推荐）/ Selenium
│   ├── JS/TS 技术栈 → Playwright（推荐）/ Cypress
│   └── 需要跨浏览器 → Playwright（推荐）/ Selenium
├── REST API → Python: requests+Pytest | JS: Axios+Jest
├── GraphQL → requests + Pytest（构造 query/mutation）
├── WebSocket → websockets + Pytest (asyncio)
├── 移动端 App
│   ├── Android → Appium (Python/Java)
│   ├── iOS → Appium (Python/Java)
│   ├── React Native → Detox (JS/TS)
│   └── Flutter → integration_test (Dart)
├── 单元测试
│   ├── Python → Pytest（推荐）/ unittest
│   ├── Java → JUnit 5
│   ├── JS/TS → Jest（推荐）/ Vitest
│   └── Go → testing 标准库
└── 性能测试
    ├── HTTP 压测 → Locust (Python) / k6 (JS)
    └── 大规模压测 → JMeter / Gatling
```

#### 选型矩阵

| 场景 | 推荐 | 备选 | 理由 |
|------|------|------|------|
| Web E2E（新） | Playwright+Pytest | Cypress | 跨浏览器、速度快 |
| Web E2E（旧Selenium） | 保持 Selenium | 渐进迁移 | 迁移成本高 |
| API 测试 | requests+Pytest | httpx+Pytest | 生态成熟 |
| 移动端 | Appium | Maestro | 跨平台 |
| 单元测试 | Pytest/Jest | unittest/Vitest | 插件丰富 |
| 性能压测 | Locust | k6 | 分布式支持 |
| 契约测试 | jsonschema+Pytest | Pact | 轻量级 |

#### 测试金字塔策略

```
         /  E2E  \          ← 少量，覆盖核心业务流程（10%）
        / 集成测试 \         ← 中量，验证模块间交互（20%）
       /  单元测试   \       ← 大量，覆盖核心逻辑（70%）
```

- **P0 冒烟测试**：核心主流程，每次提交必跑
- **P1 回归测试**：核心功能 + 关键分支，每次构建跑
- **P2 完整测试**：全量用例，每日/每周跑
- **P3 探索测试**：边缘场景，发版前手动执行

### 1.3 优先级定义

> 全技能统一定义，后续章节引用此定义。

| 优先级 | 定义 | 典型场景 |
|--------|------|---------|
| **P0 - 冒烟** | 核心功能，阻塞性测试 | 主流程、登录、核心交易 |
| **P1 - 核心** | 重要功能，影响用户体验 | 边界值、关键分支、权限控制 |
| **P2 - 一般** | 辅助功能，异常处理 | 错误提示、空状态、兼容性 |
| **P3 - 低优** | 边缘场景，极端情况 | 极端数据、并发、性能边界 |

**优先级评估维度：** 业务影响度、使用频率、风险等级、复杂度。

---

## 2. 测试用例设计与生成

> 本章职责：运用测试设计方法生成高质量测试用例。用例设计完成后，进入第 3 章编写自动化脚本。

### 2.1 测试设计方法

**等价类划分**：有效等价类（合理输入至少一个代表值）+ 无效等价类（非法输入至少一个代表值），互斥且完全覆盖。

**边界值分析**：边界上的值、边界内侧值、边界外侧值。典型边界：最小值、最大值、空值、临界长度、临界时间。

**决策表（多条件组合）**
```
条件\规则    | R1 | R2 | R3 | R4 |
------------|----|----|----|----|
条件1       | Y  | Y  | N  | N  |
条件2       | Y  | N  | Y  | N  |
------------|----|----|----|----|
预期动作    | A1 | A2 | A3 | A4 |
```

**状态转换**：识别所有状态和转换条件，覆盖所有合法转换，测试关键非法转换。

**场景法**：基本流（Happy Path）→ 备选流（分支场景）→ 异常流（异常处理和恢复）。

**错误推测**：特殊字符（中英文/emoji/SQL/XSS）、并发操作（重复提交/竞态）、网络异常（超时/断网/弱网）、大数据量（分页/搜索/导出）、时间相关（跨时区/跨天/闰年）。

### 2.2 行业测试模板

**电商**：购物车（数量边界/库存/价格）、订单（下单/支付/退款/超时）、促销（优惠券/满减）、物流（地址/运费/跟踪）。

**金融**：交易（金额精度/并发扣款/对账）、风控（黑名单/限额/异常检测）、安全（加密/审计/合规）。

**SaaS 系统**：多租户（数据隔离/配额）、权限（角色矩阵/数据权限）、订阅（计费/升降级/试用）、集成（API/Webhook）。

**社交/内容系统**：内容（审核/敏感词）、互动（点赞/关注/消息）、安全（反垃圾/隐私）、性能（高并发/缓存）。

### 2.3 用例生成规范

每个测试用例包含：
- **用例ID**：唯一标识（如 TC-MODULE-001）
- **用例标题**：格式为"动作+对象+预期"
- **优先级**：P0/P1/P2/P3（定义见 1.3）
- **前置条件** / **测试步骤**（每步一个动作）/ **测试数据**（具体值，避免占位符）
- **预期结果**：明确可客观判断的验证点
- **测试类型**：功能/性能/安全/兼容性/可用性
- **关联需求**：追溯到对应需求点

**编写原则**：独立、可重复、明确、可追溯、最小化（每用例一个测试点）、实用。

### 2.4 输出格式

#### Markdown 格式
```markdown
# 测试用例：[模块名称]
## 测试概述
- 测试模块：xxx | 用例总数：X
- 优先级分布：P0(X) / P1(X) / P2(X) / P3(X)

## 用例总览
| 用例ID | 标题 | 优先级 | 类型 | 关联需求 |
|--------|------|--------|------|---------|
| TC-XXX-001 | xxx | P0 | 功能 | REQ-001 |

### TC-XXX-001：[标题]
- **优先级**：P0 | **测试类型**：功能 | **关联需求**：REQ-001
- **前置条件**：xxx
- **测试步骤**：1. xxx  2. xxx
- **测试数据**：xxx
- **预期结果**：xxx
```

#### CSV / Excel 格式
```python
# CSV 输出
import csv
testcases = [...]  # [ID, 标题, 优先级, 类型, 前置条件, 步骤, 数据, 预期结果, 关联需求]
with open('testcases.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['用例ID','用例标题','优先级','测试类型','前置条件','测试步骤','测试数据','预期结果','关联需求'])
    writer.writerows(testcases)

# Excel 输出
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "测试用例"
headers = ['用例ID','用例标题','优先级','测试类型','前置条件','测试步骤','测试数据','预期结果','关联需求']
ws.append(headers)
header_font = Font(bold=True)
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
for cell in ws[1]:
    cell.font = header_font; cell.fill = header_fill; cell.alignment = Alignment(horizontal='center')
# 写入数据...
wb.save('testcases.xlsx')
```

### 2.5 覆盖分析

**需求覆盖率**：列出所有需求点及覆盖状态，标记未覆盖的需求点。

**测试维度覆盖：**
| 维度 | 覆盖情况 | 用例数 |
|------|---------|-------|
| 功能/边界/异常测试 | ✅ | X |
| 安全/性能/兼容性 | ✅/❌ | X |

**补充建议**：建议增加的场景、数据补充、自动化优先级。

### 2.6 用例评审 Checklist

#### 覆盖完整性
| # | 检查项 | 标准 |
|---|--------|------|
| ☐ | 所有需求点/AC 有对应用例 | 100% 覆盖 |
| ☐ | 正向流程完整 | 至少覆盖所有主流程 |
| ☐ | 反向流程覆盖 | 每功能至少 2-3 个异常场景 |
| ☐ | 边界值完整 | 有范围约束的参数都覆盖 |
| ☐ | 空值/null/零值场景 | 所有输入字段 |
| ☐ | 并发/竞态场景 | 涉及状态变更的功能 |
| ☐ | 权限控制场景 | 不同角色的访问控制 |
| ☐ | 数据精度验证 | 金额、百分比等精度敏感场景 |

#### 用例质量
| # | 检查项 | 标准 |
|---|--------|------|
| ☐ | 每用例只验证一个测试点 | 避免一个用例验证多个行为 |
| ☐ | 用例之间无依赖 | 任意顺序执行结果一致 |
| ☐ | 步骤清晰无歧义 | 新人能看懂并执行 |
| ☐ | 测试数据具体有意义 | 不使用 "aaa"、"111" |
| ☐ | 预期结果可客观判断 | 不用"正常显示"，用具体字段/值 |
| ☐ | 用例命名规范 | test_<功能>_<场景>_<预期> |

#### 优先级 & 可自动化评估
- P0 不超过 20%，P1 覆盖所有关键分支
- 标记适合自动化的用例（P0/P1 功能测试优先）
- 排除不适合自动化的（可用性/视觉检查）
- 自动化数据可独立构造，不依赖其他用例

---

## 3. 自动化测试脚本编写

> 本章职责：将测试用例转化为可运行的自动化脚本。

### 3.1 代码质量原则

- 遵循 **AAA 模式**（Arrange-Act-Assert）
- 命名清晰：`test_<功能>_<场景>_<预期>`，每用例只验证一个行为
- 使用有意义的断言消息，避免测试间依赖
- 使用 fixtures 管理测试数据和环境

### 3.2 项目结构组织

```
project/
├── src/                        # 源代码
├── tests/
│   ├── conftest.py             # 共享 fixtures
│   ├── unit/                   # 单元测试
│   ├── integration/            # 集成测试
│   ├── e2e/pages/              # E2E + Page Object
│   ├── api/                    # API 测试
│   ├── performance/locustfile.py
│   ├── utils/data_factory.py   # 数据工厂
│   └── data/test_data.json     # 测试数据
├── pytest.ini
├── requirements-test.txt
└── .github/workflows/test.yml
```

### 3.3 Page Object 模式

```python
# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    URL = "https://example.com/login"
    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    SUBMIT_BUTTON = 'button[type="submit"]'
    ERROR_MESSAGE = '.error-message'

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(self.URL); return self

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.SUBMIT_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).text_content()

    def is_login_success(self) -> bool:
        return self.page.url.endswith("/home")

# tests/e2e/test_login.py
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page).goto()

    def test_valid_login(self):
        self.login_page.login("testuser", "Test1234")
        assert self.login_page.is_login_success()

    def test_invalid_password(self):
        self.login_page.login("testuser", "wrongpass")
        assert "密码错误" in self.login_page.get_error_message()
```

### 3.4 测试数据管理

```python
# utils/data_factory.py
import faker, random
fake = faker.Faker('zh_CN')

class UserFactory:
    @staticmethod
    def create_valid_user():
        return {"username": f"user{random.randint(1000,9999)}", "password": "Test1234", "email": fake.email()}

    @staticmethod
    def create_invalid_user():
        return {"username": "user", "password": "123", "email": "invalid"}
```

### 3.5 Pytest + Playwright 模板

```python
# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser; browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(); page = context.new_page()
    yield page; context.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://example.com"
```

```ini
# pytest.ini
[pytest]
testpaths = tests
markers =
    smoke: 冒烟测试（P0）
    regression: 回归测试
    slow: 慢速测试
addopts = -v --tb=short --html=reports/report.html
```

### 3.6 性能测试 Locust 模板

```python
# tests/performance/locustfile.py
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.client.post("/login", json={"username": "testuser", "password": "Test1234"})

    @task(3)
    def view_homepage(self):
        self.client.get("/")

    @task(1)
    def view_profile(self):
        self.client.get("/profile")

    @task(2)
    def search(self):
        self.client.get("/search?q=test")
```

### 3.7 移动端 Appium 模板

```python
# tests/mobile/test_app_login.py
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMobileLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'emulator-5554'
        options.app = '/path/to/app.apk'
        options.app_package = 'com.example.app'
        options.app_activity = '.MainActivity'
        options.no_reset = True
        options.auto_grant_permissions = True
        self.driver = webdriver.Remote('http://localhost:4723', options=options)
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_valid_login(self):
        username = self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'username_input')))
        username.send_keys('testuser')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'password_input').send_keys('Test1234')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'login_button').click()
        home = self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'home_screen')))
        assert home.is_displayed()

    def test_invalid_password(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'username_input').send_keys('testuser')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'password_input').send_keys('wrongpass')
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'login_button').click()
        error = self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'error_message')))
        assert '密码错误' in error.text

    def test_biometric_login(self):
        biometric_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'biometric_login')
        biometric_btn.click()
        self.driver.toggle_biometric_auth(True)
        home = self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'home_screen')))
        assert home.is_displayed()

    def test_network_error(self):
        self.driver.toggle_wifi(False)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'login_button').click()
        error = self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'network_error')))
        assert '网络' in error.text
        self.driver.toggle_wifi(True)
```

### 3.8 CI/CD 配置

**GitHub Actions：**
```yaml
name: Test
on:
  push: {branches: [main, develop]}
  pull_request: {branches: [main]}
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with: {python-version: '3.10'}
    - run: |
        pip install -r requirements-test.txt
        playwright install --with-deps chromium
    - run: pytest tests/ -v --alluredir=allure-results
    - if: always()
      run: allure generate allure-results -o allure-report --clean
    - if: always()
      uses: actions/upload-artifact@v3
      with: {name: allure-report, path: allure-report/}
```

**GitLab CI：**
```yaml
stages: [test]
test:
  stage: test
  image: python:3.10
  script:
    - pip install -r requirements-test.txt
    - playwright install --with-deps chromium
    - pytest tests/ -v --alluredir=allure-results
  artifacts:
    when: always
    paths: [allure-results/]
```

---

## 4. API 接口测试

> 本章职责：API 全面测试（REST/GraphQL/WebSocket），含契约、Mock、性能、安全。报告生成统一引用第 6 章。

### 4.1 REST API 测试

```python
import pytest, requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class TestUserAPI:
    @pytest.fixture(autouse=True)
    def setup(self, base_url):
        self.base_url = base_url
        self.api_url = f"{base_url}/api/v1/users"
        self.session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.get_token()}"}

    def get_token(self):
        resp = requests.post(f"{self.base_url}/auth/login", json={"username":"testuser","password":"Test1234"})
        return resp.json()["access_token"]

    # === 正向测试 ===
    def test_create_user(self):
        payload = {"username":"newuser","email":"new@example.com","password":"Password123"}
        resp = self.session.post(self.api_url, json=payload, headers=self.headers)
        assert resp.status_code == 201
        data = resp.json()
        assert data["username"] == "newuser"
        assert "id" in data and "password" not in data

    def test_get_user_list(self):
        resp = self.session.get(self.api_url, headers=self.headers)
        assert resp.status_code == 200 and isinstance(resp.json(), list)

    def test_get_user_by_id(self):
        resp = self.session.get(f"{self.api_url}/1", headers=self.headers)
        assert resp.status_code == 200 and resp.json()["id"] == 1

    def test_update_user(self):
        resp = self.session.put(f"{self.api_url}/1", json={"email":"new@example.com"}, headers=self.headers)
        assert resp.status_code == 200

    def test_delete_user(self):
        resp = self.session.delete(f"{self.api_url}/999", headers=self.headers)
        assert resp.status_code in [200, 204]

    # === 参数校验 ===
    @pytest.mark.parametrize("username,error_msg", [
        ("", "用户名不能为空"), ("ab", "用户名长度至少3位"),
        ("a"*51, "用户名长度不能超过50"), ("user@#$", "用户名包含非法字符"),
    ])
    def test_invalid_username(self, username, error_msg):
        payload = {"username":username,"email":"test@example.com","password":"Password123"}
        resp = self.session.post(self.api_url, json=payload, headers=self.headers)
        assert resp.status_code == 400

    # === 异常场景 ===
    def test_not_found(self):
        assert self.session.get(f"{self.api_url}/99999", headers=self.headers).status_code == 404

    def test_duplicate_user(self):
        payload = {"username":"existing","email":"e@e.com","password":"Password123"}
        self.session.post(self.api_url, json=payload, headers=self.headers)
        assert self.session.post(self.api_url, json=payload, headers=self.headers).status_code == 409

    def test_unauthorized(self):
        assert requests.get(self.api_url).status_code == 401

    # === 性能基准 ===
    def test_response_time(self):
        import time
        start = time.time()
        resp = self.session.get(self.api_url, headers=self.headers)
        assert resp.status_code == 200 and (time.time() - start) < 1.0
```

### 4.2 GraphQL 测试

```python
class TestGraphQLAPI:
    @pytest.fixture(autouse=True)
    def setup(self, base_url):
        self.url = f"{base_url}/graphql"
        self.headers = {"Content-Type": "application/json"}

    def test_query_users(self):
        query = 'query { users { id username email } }'
        resp = requests.post(self.url, json={"query": query}, headers=self.headers)
        assert resp.status_code == 200 and "users" in resp.json()["data"]

    def test_mutation_create_user(self):
        mutation = """mutation CreateUser($input: CreateUserInput!) {
            createUser(input: $input) { id username email } }"""
        variables = {"input": {"username":"newuser","email":"new@example.com","password":"Password123"}}
        resp = requests.post(self.url, json={"query":mutation,"variables":variables}, headers=self.headers)
        assert resp.json()["data"]["createUser"]["username"] == "newuser"
```

### 4.3 WebSocket 测试

```python
import pytest, asyncio, websockets, json

class TestWebSocketAPI:
    @pytest.fixture
    def ws_url(self): return "ws://localhost:8080/ws"

    @pytest.mark.asyncio
    async def test_connect(self, ws_url):
        async with websockets.connect(ws_url) as ws:
            assert ws.open
            msg = await asyncio.wait_for(ws.recv(), timeout=5)
            assert json.loads(msg)["type"] == "connected"

    @pytest.mark.asyncio
    async def test_send_receive(self, ws_url):
        async with websockets.connect(ws_url) as ws:
            await ws.send(json.dumps({"action":"subscribe","channel":"updates"}))
            resp = await asyncio.wait_for(ws.recv(), timeout=5)
            data = json.loads(resp)
            assert data["action"] == "subscribed" and data["channel"] == "updates"

    @pytest.mark.asyncio
    async def test_broadcast(self, ws_url):
        async with websockets.connect(ws_url) as ws1, websockets.connect(ws_url) as ws2:
            await ws1.send(json.dumps({"action":"broadcast","message":"hello"}))
            resp = await asyncio.wait_for(ws2.recv(), timeout=5)
            assert json.loads(resp)["message"] == "hello"

    @pytest.mark.asyncio
    async def test_invalid_message(self, ws_url):
        async with websockets.connect(ws_url) as ws:
            await ws.send("invalid json{{{")
            data = json.loads(await asyncio.wait_for(ws.recv(), timeout=5))
            assert data["type"] == "error"

    @pytest.mark.asyncio
    async def test_unauthorized(self):
        with pytest.raises(websockets.exceptions.InvalidStatusCode) as exc:
            async with websockets.connect("ws://localhost:8080/ws/protected"): pass
        assert exc.value.status_code == 401

    @pytest.mark.asyncio
    async def test_heartbeat(self, ws_url):
        async with websockets.connect(ws_url) as ws:
            for _ in range(3):
                msg = await asyncio.wait_for(ws.recv(), timeout=35)
                if json.loads(msg).get("type") == "ping":
                    await ws.send(json.dumps({"type": "pong"}))

    @pytest.mark.asyncio
    async def test_concurrent(self, ws_url):
        conns = [await websockets.connect(ws_url) for _ in range(100)]
        assert all(ws.open for ws in conns)
        for ws in conns: await ws.close()
```

### 4.4 从 OpenAPI 生成测试

```python
import json, yaml

def generate_tests_from_openapi(spec_path):
    with open(spec_path) as f:
        spec = yaml.safe_load(f) if spec_path.endswith('.yaml') else json.load(f)
    tests, base_url = [], spec.get('servers',[{}])[0].get('url','')
    for path, methods in spec.get('paths',{}).items():
        for method, details in methods.items():
            if method not in ['get','post','put','delete','patch']: continue
            test = {"path":path,"method":method.upper(),"summary":details.get('summary',''),"parameters":[],"request_body":None,"responses":details.get('responses',{})}
            for param in details.get('parameters',[]):
                test["parameters"].append({"name":param.get('name'),"in":param.get('in'),"required":param.get('required',False),"type":param.get('schema',{}).get('type','string')})
            if 'requestBody' in details:
                content = details['requestBody'].get('content',{})
                if 'application/json' in content:
                    test["request_body"] = content['application/json'].get('schema',{})
            tests.append(test)
    return tests
```

### 4.5 契约测试

```python
import jsonschema

class TestContractTesting:
    @pytest.fixture
    def user_schema(self):
        return {
            "type":"object", "required":["id","username","email","created_at"],
            "properties":{
                "id":{"type":"integer"},
                "username":{"type":"string","minLength":3,"maxLength":50},
                "email":{"type":"string","format":"email"},
                "created_at":{"type":"string","format":"date-time"}
            },
            "additionalProperties": False
        }

    def test_user_response_contract(self, user_schema):
        data = requests.get(f"{self.base_url}/api/users/1").json()
        jsonschema.validate(instance=data, schema=user_schema)

    def test_user_list_contract(self):
        data = requests.get(f"{self.base_url}/api/users").json()
        assert isinstance(data, list)
        for user in data: jsonschema.validate(instance=user, schema=self.user_schema())
```

### 4.6 Mock 服务

```python
from flask import Flask, jsonify, request
import threading

class MockServer:
    def __init__(self, port=5001):
        self.app = Flask(__name__); self.port = port
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/api/users', methods=['GET'])
        def get_users():
            return jsonify([{"id":1,"username":"user1","email":"u1@ex.com"},{"id":2,"username":"user2","email":"u2@ex.com"}])

        @self.app.route('/api/users/<int:uid>', methods=['GET'])
        def get_user(uid):
            if uid == 999: return jsonify({"error":"Not found"}), 404
            return jsonify({"id":uid,"username":f"user{uid}","email":f"u{uid}@ex.com"})

        @self.app.route('/api/users', methods=['POST'])
        def create_user():
            data = request.get_json()
            if not data.get('username'): return jsonify({"error":"用户名不能为空"}), 400
            return jsonify({"id":3,"username":data['username'],"email":data.get('email',''),"created_at":"2024-01-01T00:00:00Z"}), 201

        @self.app.route('/api/users/<int:uid>', methods=['PUT'])
        def update_user(uid):
            data = request.get_json()
            return jsonify({"id":uid,"username":data.get('username',f"user{uid}"),"email":data.get('email',f"u{uid}@ex.com")})

        @self.app.route('/api/users/<int:uid>', methods=['DELETE'])
        def delete_user(uid): return '', 204

    def start(self):
        t = threading.Thread(target=lambda: self.app.run(port=self.port, debug=False))
        t.daemon = True; t.start(); return self
```

### 4.7 API 性能基准测试

```python
import time, statistics
from concurrent.futures import ThreadPoolExecutor

class TestAPIPerformance:
    def test_latency(self):
        latencies = []
        for _ in range(100):
            s = time.time(); requests.get(f"{self.base_url}/api/users"); latencies.append((time.time()-s)*1000)
        print(f"平均:{statistics.mean(latencies):.2f}ms P50:{statistics.median(latencies):.2f}ms P95:{sorted(latencies)[95]:.2f}ms")
        assert statistics.mean(latencies) < 500

    def test_concurrent(self):
        start = time.time()
        with ThreadPoolExecutor(max_workers=50) as ex:
            results = list(ex.map(lambda _: requests.get(f"{self.base_url}/api/users").status_code, range(500)))
        duration = time.time() - start
        qps = 500 / duration
        success = sum(1 for r in results if r == 200)
        print(f"QPS:{qps:.2f} 成功率:{success/500*100:.1f}%")
        assert success/500 > 0.99 and qps > 100
```

### 4.8 安全测试

```python
class TestAPISecurity:
    def test_sql_injection(self):
        for payload in ["' OR '1'='1", "'; DROP TABLE users; --", "1 UNION SELECT * FROM users"]:
            resp = requests.get(f"{self.base_url}/api/users", params={"search": payload})
            assert resp.status_code in [400, 403, 500]

    def test_xss_injection(self):
        for payload in ["<script>alert('xss')</script>", "<img src=x onerror=alert('xss')>"]:
            resp = requests.post(f"{self.base_url}/api/users", json={"username":payload,"email":"t@e.com"})
            assert payload not in resp.text

    def test_auth_bypass(self):
        for h in [{}, {"Authorization":"Bearer invalid"}, {"Authorization":"Bearer "}]:
            assert requests.get(f"{self.base_url}/api/users", headers=h).status_code in [401, 403]

    def test_rate_limiting(self):
        codes = [requests.get(f"{self.base_url}/api/users").status_code for _ in range(150)]
        assert 429 in codes
```

---

## 5. 缺陷分析与追踪

> 本章职责：缺陷根因分析、分类、模式识别、趋势分析，集成 Jira/禅道。深度 RCA 使用本章方法，报告中的数据层面失败模式见第 6 章。

### 5.1 根因分析 RCA（5 Whys）

```
问题现象 → Why? → 直接原因 → Why? → 中间原因 → ... → 根本原因
```

**RCA 报告模板：**
```markdown
## Bug 根因分析报告
### 问题描述
- **现象**：xxx | **影响范围**：xxx
- **严重程度**：S1/S2/S3/S4（定义见 5.2）| **优先级**：P0-P3（定义见 1.3）

### 5 Whys 分析
1. Why [现象]？ → [直接原因]
2. Why [直接原因]？ → [中间原因]
3. Why [中间原因]？ → [中间原因2]
4. Why [中间原因2]？ → [中间原因3]
5. Why [中间原因3]？ → [根本原因]

### 修复方案
- **短期修复**：xxx | **长期修复**：xxx | **预防措施**：xxx
```

### 5.2 Bug 分类体系

#### 按类型
| 类型 | 定义 | 示例 |
|------|------|------|
| 功能缺陷 | 功能不符合需求规格 | 登录失败、计算错误 |
| 界面缺陷 | UI 显示异常 | 布局错乱、文案错误 |
| 性能缺陷 | 响应慢、资源占用高 | 加载超时、内存泄漏 |
| 安全缺陷 | 存在安全隐患 | SQL注入、XSS、越权 |
| 兼容性缺陷 | 特定环境异常 | 浏览器兼容、移动端适配 |
| 数据缺陷 | 数据处理问题 | 数据丢失、精度错误 |
| 接口缺陷 | API 调用异常 | 返回错误、参数校验失败 |

#### 按严重程度
| 等级 | 定义 | 响应时间 |
|------|------|---------|
| **致命（S1）** | 系统崩溃/数据丢失/核心不可用 | 立即修复 |
| **严重（S2）** | 主要功能异常/性能严重下降 | 24小时内 |
| **一般（S3）** | 次要功能异常/有替代方案 | 3天内 |
| **轻微（S4）** | 界面瑕疵/文案错误 | 排期修复 |

#### 优先级修复策略（定义见 1.3）
P0 立即修复暂停其他工作 | P1 当前迭代修复 | P2 计划修复 | P3 排期修复

### 5.3 Bug 模式识别

```python
def analyze_bug_patterns(bugs):
    patterns = {"by_module":{}, "by_type":{}, "by_severity":{}, "recurring":[], "clusters":[]}
    for bug in bugs:
        m = bug.get("module","未分类")
        patterns["by_module"][m] = patterns["by_module"].get(m, 0) + 1
    for i, b1 in enumerate(bugs):
        for b2 in bugs[i+1:]:
            if is_similar_bug(b1, b2): patterns["recurring"].append((b1, b2))
    return patterns
```

| 模式 | 特征 | 可能根因 |
|------|------|---------|
| 边界值集中 | 大量 Bug 在边界条件 | 边界测试不足 |
| 模块热点 | 某模块 Bug 密集 | 代码复杂度高或开发质量差 |
| 回归Bug | 修复后再次出现 | 修复不彻底或缺少回归测试 |
| 环境相关 | 特定环境才出现 | 环境配置差异 |
| 数据相关 | 特定数据才出现 | 数据边界处理不完善 |

### 5.4 Bug 报告模板

```markdown
# Bug 报告：[标题]
| 字段 | 值 |
|------|-----|
| Bug ID | BUG-XXX-001 |
| 严重程度 | S1/S2/S3/S4 |
| 优先级 | P0-P3（定义见 1.3）|
| 所属模块 | xxx |
| 发现版本 | v1.2.3 |
| 状态 | 新建/处理中/已修复/已验证/已关闭 |

**现象**：xxx | **影响范围**：xxx
**重现步骤**：1. xxx  2. xxx  3. xxx
**预期结果**：xxx | **实际结果**：xxx
**环境**：OS/Browser/Version
**附件**：截图/录屏/日志
**RCA**：[5 Whys 分析结果]
**修复方案**：短期 xxx | 长期 xxx
```

### 5.5 缺陷趋势分析

| 指标 | 计算方式 | 说明 |
|------|---------|------|
| 缺陷密度 | Bug数/代码行数 | 代码质量 |
| 缺陷发现率 | 本期发现/总预估 | 测试有效性 |
| 缺陷修复率 | 已修复/总Bug数 | 修复效率 |
| 缺陷收敛率 | (发现-修复)/发现 | 收敛趋势 |
| 平均修复时长 | Σ修复时长/Bug数 | 响应效率 |
| 重新打开率 | 重新打开/已关闭 | 修复质量 |

```python
def analyze_defect_trend(history):
    trend = {"discovery_rate":[],"fix_rate":[],"convergence":[],"backlog":[]}
    for p in history:
        d, f, t = p["new_bugs"], p["fixed_bugs"], p["total_bugs"]
        trend["discovery_rate"].append(d/t*100)
        trend["fix_rate"].append(f/d*100 if d>0 else 0)
        trend["convergence"].append((d-f)/d*100 if d>0 else 0)
        trend["backlog"].append(t-f)
    return trend
```

### 5.6 缺陷管理工具集成

#### Jira 集成
```python
from coze_workload_identity import requests
import os

class JiraClient:
    def __init__(self):
        self.base_url = os.getenv("COZE_JIRA_API_URL")
        self.headers = {"Authorization":f"Bearer {os.getenv('JIRA_API_TOKEN')}","Content-Type":"application/json"}

    def get_bugs(self, jql="project = XXX AND type = Bug"):
        return requests.get(f"{self.base_url}/rest/api/3/search", headers=self.headers, params={"jql":jql,"maxResults":100}).json()

    def create_bug(self, summary, description, priority, labels=None):
        data = {"fields":{"project":{"key":"XXX"},"summary":summary,"description":description,"issuetype":{"name":"Bug"},"priority":{"name":priority},"labels":labels or []}}
        return requests.post(f"{self.base_url}/rest/api/3/issue", headers=self.headers, json=data).json()
```

#### 禅道集成
```python
class ZenTaoClient:
    def __init__(self):
        self.base_url = os.getenv("COZE_ZENTAO_URL")
        self.token = os.getenv("ZENTAO_API_TOKEN")

    def get_bugs(self, product_id):
        return requests.get(f"{self.base_url}/api.php/v1/products/{product_id}/bugs", headers={"Token":self.token}).json()
```

---

## 6. 测试报告生成

> 本章职责：从测试执行数据生成多格式可视化报告。数据层失败模式识别在本章，深度 RCA 引用第 5 章。

### 6.1 数据解析

| 输入类型 | 格式 | 解析方式 |
|---------|------|---------|
| Pytest | XML/JSON | JUnit XML 或 JSON 报告 |
| Allure | allure-results 目录 | JSON 结果文件 |
| Jest | JSON | --json 输出 |
| JUnit XML | .xml | 标准 JUnit 格式 |
| 手动数据/日志 | Markdown/table/.log | 结构提取/正则提取 |

```python
import xml.etree.ElementTree as ET

def parse_pytest_xml(file_path):
    root = ET.parse(file_path).getroot()
    results = {"total":0,"passed":0,"failed":0,"skipped":0,"errors":0,"duration":0,"test_cases":[]}
    for ts in root.findall('.//testsuite'):
        results["total"] += int(ts.get("tests",0))
        results["failed"] += int(ts.get("failures",0))
        results["errors"] += int(ts.get("errors",0))
        results["skipped"] += int(ts.get("skipped",0))
        results["duration"] += float(ts.get("time",0))
        for tc in ts.findall('testcase'):
            case = {"name":tc.get("name"),"classname":tc.get("classname"),"time":float(tc.get("time",0)),"status":"passed"}
            if tc.find('failure') is not None: case["status"]="failed"; case["error_message"]=tc.find('failure').get("message")
            elif tc.find('skipped') is not None: case["status"]="skipped"
            results["test_cases"].append(case)
    results["passed"] = results["total"]-results["failed"]-results["skipped"]-results["errors"]
    return results
```

### 6.2 核心指标

| 指标 | 计算方式 | 说明 |
|------|---------|------|
| 通过率 | passed/total×100% | 核心质量指标 |
| 执行效率 | total/duration | 每秒执行用例数 |
| 失败集中度 | 失败模块/总模块 | 问题集中区域 |
| 平均执行时间 | duration/total | 单用例耗时 |
| 回归率 | 新增失败/上次通过 | 质量回归程度 |

### 6.3 Markdown 报告

```markdown
# 测试报告
**执行时间**：2024-01-15 10:30 | **总耗时**：125.6s | **环境**：Python 3.10 / Chrome 120

## 📊 概览
| 指标 | 数值 | 趋势 |
|------|------|------|
| 总用例 | 256 | ↑ +12 |
| 通过/失败/跳过 | 241/12/3 | |
| **通过率** | **94.1%** | ↑ +2.3% |

## ❌ 失败分析
| 模块 | 失败数 | 占比 | | 用例 | 错误类型 | 错误信息 |
|------|--------|------|-|------|---------|---------|
| 登录模块 | 5 | 41.7% | | test_login_timeout | Timeout | 页面加载超时 |
| 支付模块 | 4 | 33.3% | | test_payment_verify | AssertionError | 金额不匹配 |

## ⏱️ 性能 Top 5
| 用例 | 耗时 | 状态 |
|------|------|------|
| test_import_data | 15.2s | ✅ |
| test_export_report | 12.8s | ✅ |

## 📈 建议
1. 登录模块失败率较高，建议优先排查
2. test_import_data 执行时间过长，建议优化
```

### 6.4 HTML 报告（带图表）

```python
import json
from datetime import datetime

def generate_html_report(data, output_path):
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<title>测试报告 - {datetime.now().strftime('%Y-%m-%d')}</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body{{font-family:-apple-system,sans-serif;margin:40px;background:#f5f5f5}}
.container{{max-width:1200px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:30px;border-radius:12px;margin-bottom:20px}}
.card{{background:#fff;border-radius:12px;padding:24px;margin-bottom:20px;box-shadow:0 2px 8px rgba(0,0,0,.1)}}
.metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}
.metric{{text-align:center;padding:20px;background:#f8f9fa;border-radius:8px}}
.metric-value{{font-size:32px;font-weight:bold;color:#333}}
.metric-label{{color:#666;margin-top:8px}}
.pass{{color:#22c55e}} .fail{{color:#ef4444}}
table{{width:100%;border-collapse:collapse}} th,td{{padding:12px;text-align:left;border-bottom:1px solid #eee}}
th{{background:#f8f9fa;font-weight:600}} .chart-container{{height:300px}}
</style></head><body><div class="container">
<div class="header"><h1>📋 测试报告</h1><p>生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p></div>
<div class="card"><h2>📊 测试概览</h2><div class="metrics">
<div class="metric"><div class="metric-value">{data['total']}</div><div class="metric-label">总用例</div></div>
<div class="metric"><div class="metric-value pass">{data['passed']}</div><div class="metric-label">通过</div></div>
<div class="metric"><div class="metric-value fail">{data['failed']}</div><div class="metric-label">失败</div></div>
<div class="metric"><div class="metric-value">{data['pass_rate']:.1f}%</div><div class="metric-label">通过率</div></div>
</div></div>
<div class="card"><h2>📈 结果分布</h2><div class="chart-container"><canvas id="pieChart"></canvas></div></div>
<div class="card"><h2>❌ 失败用例详情</h2><table><thead><tr><th>#</th><th>用例名称</th><th>模块</th><th>错误类型</th><th>错误信息</th><th>严重程度</th></tr></thead><tbody>
{''.join(f'<tr><td>{i+1}</td><td>{c["name"]}</td><td>{c.get("module","-")}</td><td>{c.get("error_type","-")}</td><td>{c.get("error_message","-")}</td><td>{c.get("severity","-")}</td></tr>' for i,c in enumerate(data.get('failed_cases',[])))}
</tbody></table></div>
<div class="card"><h2>⏱️ 性能分析 - 最慢 Top 10</h2><div class="chart-container"><canvas id="barChart"></canvas></div>
<table><thead><tr><th>#</th><th>用例名称</th><th>耗时(s)</th><th>状态</th></tr></thead><tbody>
{''.join(f'<tr><td>{i+1}</td><td>{c["name"]}</td><td>{c["time"]:.2f}</td><td>{"✅" if c["status"]=="passed" else "❌"}</td></tr>' for i,c in enumerate(data.get('slowest_cases',[])[:10]))}
</tbody></table></div>
<div class="card"><h2>🔍 失败模式分析</h2><table><thead><tr><th>失败模式</th><th>次数</th><th>占比</th><th>修复建议</th></tr></thead><tbody>
{''.join(f'<tr><td>{p["pattern"]}</td><td>{p["count"]}</td><td>{p["percentage"]:.1f}%</td><td>{p["suggestion"]}</td></tr>' for p in data.get('failure_patterns',[]))}
</tbody></table></div>
<div class="card"><h2>💡 修复建议</h2><ol>{''.join(f'<li>{s}</li>' for s in data.get('suggestions',[]))}</ol></div>
<div class="card"><h2>📋 发布结论</h2>
<p style="font-size:18px;font-weight:bold;color:{data.get('release_color','#333')}">{data.get('release_verdict','待定')}</p>
<p>{data.get('release_note','')}</p></div></div>
<script>
new Chart(document.getElementById('pieChart'),{{type:'doughnut',data:{{labels:['通过','失败','跳过'],datasets:[{{data:[{data['passed']},{data['failed']},{data['skipped']}],backgroundColor:['#22c55e','#ef4444','#94a3b8']}}]}},options:{{responsive:true,plugins:{{legend:{{position:'bottom'}}}}}}}});
new Chart(document.getElementById('barChart'),{{type:'bar',data:{{labels:{json.dumps([c['name'] for c in data.get('slowest_cases',[])[:10]],ensure_ascii=False)},datasets:[{{label:'耗时(秒)',data:{json.dumps([round(c['time'],2) for c in data.get('slowest_cases',[])[:10]])},backgroundColor:'#6366f1'}}]}},options:{{responsive:true,indexAxis:'y',plugins:{{legend:{{display:false}}}}}}}});
</script></body></html>"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    return output_path
```

### 6.5 Excel 报告

```python
import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.chart import PieChart, Reference

def generate_excel_report(data, output_path):
    wb = openpyxl.Workbook()
    ws = wb.active; ws.title = "测试概览"
    hfont = Font(bold=True, color="FFFFFF")
    hfill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

    ws['A1'] = "测试报告"; ws['A1'].font = Font(size=16, bold=True)
    ws['A3'], ws['B3'] = "指标", "数值"
    for c in ws[3]: c.font = hfont; c.fill = hfill

    for i, (label, val) in enumerate([("总用例数",data['total']),("通过",data['passed']),("失败",data['failed']),("跳过",data['skipped']),("通过率",f"{data['pass_rate']:.1f}%"),("执行时间",f"{data['duration']:.1f}s")], 4):
        ws[f'A{i}'], ws[f'B{i}'] = label, val

    pie = PieChart(); pie.title = "测试结果分布"
    pie.add_data(Reference(ws, min_col=2, min_row=4, max_row=6))
    pie.set_categories(Reference(ws, min_col=1, min_row=4, max_row=6))
    ws.add_chart(pie, "D3")

    if data.get('failed_cases'):
        ws2 = wb.create_sheet("失败用例")
        ws2.append(["用例ID","用例名称","模块","错误类型","错误信息"])
        for c in ws2[1]: c.font = hfont; c.fill = hfill
        for case in data['failed_cases']: ws2.append([case['id'],case['name'],case['module'],case['error_type'],case['message']])

    wb.save(output_path); return output_path
```

### 6.6 趋势分析

```python
def analyze_trend(history_data):
    trend = {"pass_rate_trend":[],"total_trend":[],"duration_trend":[],"quality_score":0}
    for run in history_data:
        trend["pass_rate_trend"].append(run["pass_rate"])
        trend["total_trend"].append(run["total"])
        trend["duration_trend"].append(run["duration"])
    avg = sum(trend["pass_rate_trend"])/len(trend["pass_rate_trend"])
    stability = 100-(max(trend["pass_rate_trend"])-min(trend["pass_rate_trend"]))
    trend["quality_score"] = avg*0.6 + stability*0.4
    return trend
```

**失败模式识别（数据层面）：**
| 失败模式 | 识别特征 | 建议 |
|---------|---------|------|
| 超时失败 | "timeout"、"超时" | 增加等待或优化性能 |
| 断言失败 | "assert"、"expected" | 检查业务逻辑或测试数据 |
| 元素定位 | "not found"、"unable to locate" | 更新选择器或检查页面 |
| 网络错误 | "connection"、"network"、"503" | 检查网络或服务状态 |
| 数据问题 | "null"、"undefined"、"empty" | 检查测试数据准备 |

> 深度根因分析（RCA）方法见第 5 章。

---

## 7. 测试调试与优化

> 本章职责：分析测试失败原因并提供修复方案，优化测试代码质量和效率。

### 7.1 测试调试

1. **收集信息**：错误日志、失败截图（UI测试）、测试环境和数据
2. **分析错误类型**：

   | 错误类型 | 常见原因 | 排查方向 |
   |---------|---------|---------|
   | 断言失败 | 预期值与实际值不符 | 检查业务逻辑、测试数据 |
   | 元素定位失败 | 选择器变化、元素未加载 | 更新选择器、增加等待 |
   | 超时错误 | 页面加载慢、网络问题 | 增加超时、优化等待策略 |
   | 环境问题 | 配置错误、依赖缺失 | 检查配置、安装依赖 |
   | 数据问题 | 测试数据不存在或过期 | 用 fixture 重新创建数据 |

3. **提供修复方案**：给出具体代码修改建议

### 7.2 测试优化

| 问题类型 | 症状 | 优化方案 |
|---------|------|---------|
| 执行速度慢 | 运行时间过长 | 并行执行、优化等待策略 |
| 测试不稳定（Flaky） | 时过时不过 | 重试机制、改进定位、避免竞态 |
| 代码重复 | 多个用例相同代码 | 提取公共 fixtures 和辅助函数 |
| 断言不充分 | 通过但实际有问题 | 补充边界条件和异常场景 |
| 维护困难 | 页面变化导致大量失败 | 使用 Page Object 模式 |

---

## 8. 通用规范

> 本章职责：全技能通用的框架矩阵、输出规范和注意事项。

### 8.1 框架支持矩阵

| 测试类型 | Python | JavaScript/TypeScript |
|---------|--------|---------------------|
| 单元测试 | Pytest, unittest | Jest, Mocha |
| Web E2E | Playwright, Selenium | Playwright, Cypress |
| API 测试 | requests + Pytest | Axios + Jest |
| 移动端 | Appium | Detox |
| 性能测试 | Locust | k6 |

### 8.2 输出规范

1. **代码可直接运行**：不留 TODO 或占位符
2. **使用显式等待**：Web UI 用 `wait_for_*` 而非 `sleep`
3. **有意义的命名**：测试方法名体现测试意图
4. **完整的注释**：关键逻辑添加注释
5. **错误处理**：适当异常捕获和错误提示

### 8.3 注意事项

- 优先使用用户已安装的测试框架；Web UI 始终用 Page Object 模式
- 代码可通过 flake8/eslint；测试数据用 factory 模式，避免硬编码
- API 测试覆盖正向/反向/边界/异常；参数校验穷举非法输入
- 性能测试在独立环境，明确响应时间/吞吐量/并发数指标
- Mock 定期同步真实接口；契约测试随文档更新；安全测试不危害生产
- 用例数量：简单功能 10-15 个，复杂 20-40 个；优先核心功能和高风险
- 安全用例覆盖 OWASP Top 10；涉及金额必须含精度测试
- 已有用例基础上补充，保持风格一致
- 根因分析追到根本原因；Bug 分类一致；趋势分析有对比基准
- 质量预测仅供参考；修复方案区分短期和长期
- 报告关键指标突出；失败分析提供可操作建议
- HTML 报告确保浏览器兼容；Excel 设好列宽样式
- 大量用例支持分页/分模块；Allure 报告详见 6.4

### 8.4 缺陷分析报告模板

包含：概览（总Bug/修复率/平均修复时长 + 趋势）、热点模块 Top 5、根因分析摘要（按类型分布）、质量预测（基于收敛率）、改进建议。格式参考 Markdown 报告模板（见 6.3）。
