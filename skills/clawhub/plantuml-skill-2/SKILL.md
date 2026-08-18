---
name: "plantuml"
description: "用 PlantUML 文本语法绘制 UML 图：时序图、类图、活动图、用例图、状态图、组件图、部署图、思维导图、甘特图等。"
---

# PlantUML 图表绘制

使用 PlantUML 基于文本的语法生成 UML 图和其他图表类型。所有图表都以 `@startuml` 开始，以 `@enduml` 结束。

## 基本结构

```
@startuml
' 图表内容
@enduml
```

注释：单行用 `'`，块注释用 `/' ... '/`。

## 通用命令

- `title` — 添加标题
- `caption` — 图片下方标题
- `header` / `footer` — 页眉/页脚（可加 `left`/`center`/`right`）
- `legend` ... `end legend` — 图例
- `scale 1.5` / `scale 200 width` / `scale 200*100` — 缩放
- `left to right direction` — 改变方向
- Creole 语法可用于文本格式化（粗体 `**...**`、斜体 `//...//`、列表等）

## 时序图 (Sequence Diagram)

### 参与者声明

```
participant Alice
actor Bob
boundary Wall
control C
entity E
database DB
collections Col
queue Q
```

用 `as` 定义别名：`participant Alice as A`。
用 `order` 设定顺序：`participant Alice order 10`。

### 消息箭头

- `A -> B` — 实线箭头
- `A --> B` — 虚线箭头
- `A <- B` — 反向
- `A ->> B` — 实线开放箭头
- `A -\ B` — 仅起始端箭头
- `A \\- B` — 仅末端箭头
- `A x> B` — 末端带X
- `A -> B : 消息文本` — 带标签

### 生命线

- `activate A` / `deactivate A`
- `autoactivate on` — 自动激活
- `destroy A` — 销毁

### 分组

- `alt/else` — 条件分支
- `opt` — 可选
- `loop` — 循环
- `par` — 并行
- `break` — 中断
- `critical` — 关键
- `group 标题` — 自定义分组

### 其他

- `note left/right/over` — 注释
- `A -> B : <text>` 中可使用 `\n` 换行
- `ref over A, B` — 引用
- `delay` — 延迟
- `divider` — 分隔线

## 类图 (Class Diagram)

### 元素声明

```
class ClassName {
  + publicMethod()
  - privateField: Type
  # protectedField: Type
  ~ packageField: Type
  {static} staticField
  {abstract} abstractMethod()
}
interface InterfaceName
abstract class AbstractClass
enum EnumName {
  VALUE1
  VALUE2
}
annotation AnnotationName
```

可见性：`+` public, `-` private, `#` protected, `~` package。

### 关系

- `A --|> B` — 继承（A继承B）
- `A ..|> B` — 实现（A实现B接口）
- `A --> B` — 关联
- `A --* B` — 组合
- `A ..* B` — 聚合
- `A o-- B` — 聚合（反向）
- `A ..> B` — 依赖
- `A -- B` — 实线连接
- `A .. B` — 虚线连接

关系标签：`A --> "1" B : "包含"`，`"*" --> "1"` 多重性。

### 构造型与注释

```
<<interface>> InterfaceName
<<abstract>> AbstractClass
<<enumeration>> EnumName
<<annotation>> AnnotationName
```

类内注释：`note left`, `note right`, `note top`, `note bottom`。

### 包

```
package "包名" {
  class A
  class B
}
```

## 活动图 (Activity Diagram, Beta)

### 基本语法

```
@startuml
start
:动作1;
:动作2;
stop
@enduml
```

动作以 `:` 开始，`;` 结束。隐式自动连接。

### 条件

```
if (条件?) then (yes)
  :动作A;
else (no)
  :动作B;
endif
```

`elseif` 支持多分支。`!pragma useVerticalIf on` 切换垂直模式。

### Switch

```
switch (变量?)
case (值1)
  :动作1;
case (值2)
  :动作2;
endswitch
```

### 循环

```
repeat
  :动作;
repeat while (条件?)
```

```
while (条件?) is (标签)
  :动作;
endwhile
```

### 并行

```
fork
  :分支1;
fork again
  :分支2;
end fork
```

### 分割

```
split
  :路径1;
split again
  :路径2;
end split
```

### 泳道

```
|泳道A|
:动作1;
|泳道B|
:动作2;
```

泳道别名：`|#<颜色>|<别名>| <标题>`。

### 分组

```
partition "分区名" {
  :动作1;
  :动作2;
}
```

也支持 `group`, `package`, `rectangle`, `card`。

### 其他

- `kill` / `detach` — 终止/分离
- `break` — 打断循环
- `note` — 注释（可用 `floating` 浮动）
- 箭头：`->` 可加文本和颜色

## 用例图 (Use Case Diagram)

### 语法

```
actor 用户 as U
usecase "登录" as UC1
usecase "查看资料" as UC2
U --> UC1
U --> UC2
UC1 ..> UC2 : <<include>>
```

- Actor：`actor` 关键字或冒号语法 `:用户名:`
- 用例：`usecase` 关键字或括号 `(用例名)`
- `as` 定义别名
- 矩形：`rectangle "系统名" { ... }` 分组

### 关系

- `-->` 关联
- `..> ` 依赖
- `..> : <<include>>` 包含
- `..> : <<extend>>` 扩展
- `--|>` 继承

## 状态图 (State Diagram)

### 基本语法

```
[*] --> State1
State1 --> State2 : 事件
State2 --> [*]
```

### 复合状态

```
state Composite {
  state Sub1
  state Sub2
  Sub1 --> Sub2
}
```

### 伪状态

- `<<fork>>` / `<<join>>` — 分叉/合并
- `<<choice>>` — 选择
- `<<entryPoint>>` / `<<exitPoint>>` — 入口/出口
- `[H]` / `[H*]` — 历史/深历史状态

### 并发

用 `--` 或 `||` 分隔并发区域。

### 注释

`note left of`, `note right of`, `note top of`, `note bottom of`, `note on link`。

## 组件图 (Component Diagram)

### 语法

```
component "组件A" as A
component [组件B]
interface "接口" as I
A --|> I
A ..> B : 使用
```

- 组件：`component` 或 `[名称]`
- 接口：`interface` 或 `()名称`
- `as` 别名

### 连接类型

- `..` 虚线
- `--` 实线
- `-->` 箭头

### 分组容器

`package`, `node`, `folder`, `frame`, `cloud`, `database`。

### 端口

`port`, `portIn`, `portOut` 关键字。

## 部署图 (Deployment Diagram)

### 元素

```
actor 用户
component 组件
interface 接口
usecase 用例
node 服务器 {
  component 应用
}
database 数据库
```

短格式：`:a:` (actor), `[c]` (component), `()i` (interface), `(u)` (usecase)。

### 连接

与组件图相同的连接类型，支持线条样式、颜色、粗细。

### 嵌套

所有元素可嵌套：`node`, `package`, `folder`, `frame`, `cloud`, `database`。

`allowmixing` 或 `allow_mixing` 指令允许在类图/对象图中混用部署元素。

## 时序图/定时图 (Timing Diagram)

### 参与者类型

- `analog` — 模拟信号（连续，线性插值）
- `binary` — 二进制信号
- `clock` — 时钟信号（需 `period`，可选 `pulse`/`offset`）
- `concise` — 简明表示
- `robust` — 状态线表示

### 语法

```
@startuml
clock clk period 2
binary b
robust r
@0
b is high
r is state1
@5
b is low
r is state2
@enduml
```

- `@N` — 绝对时间
- `@+N` / `@-N` — 相对时间
- `@N as :名称` — 锚点
- `is` — 定义状态

## 思维导图 (MindMap)

### 语法（运算符方式）

```
@startmindmap
+ 中心主题
++ 一级分支
+++ 二级分支
-- 左侧分支
--- 二级左侧
@endmindmap
```

运算符：`+` 右侧, `-` 左侧, `*` 右侧多级, `_` 左侧多级。

### OrgMode 语法

```
@startmindmap
* 中心
** 分支1
*** 子分支
@endmindmap
```

### Markdown 语法

```
@startmindmap
- 中心
-- 分支
--- 子分支
@endmindmap
```

多行文本用 `:` 和 `;` 包围。

## 甘特图 (Gantt Diagram)

### 语法

```
@startgantt
projectstart 2024-01-01
[任务A] lasts 5 days
[任务B] lasts 3 days
[任务B] starts at [任务A]'s end
@endgantt
```

### 关键命令

- `[任务] lasts N days` — 持续时间
- `[任务] starts N days after [任务B]'s end` — 相对开始
- `[任务] ends at [任务B]'s end` — 相对结束
- `[任务] happens at 2024-01-15` — 绝对日期
- `then` — 连续任务
- `[任务] as T` — 短名称
- `is xx% completed` — 完成度
- `[里程碑] happens at 2024-02-01` — 里程碑

### 日历

- `projectstart` — 项目开始日期
- `2024-01-01 to 2024-12-31` — 日期范围
- `saturday are closed` / `sunday are closed` — 关闭日
- `printscale daily/weekly/monthly/quarterly/yearly` — 尺度

## 主题（!theme）

PlantUML 内置了多套预设主题，用 `!theme` 指令即可一键切换整套配色/字体/形状，不用手动调 skinparam。

```
@startuml
!theme cyborg
class Foo
@enduml
```

`!theme` 通常放在 `@startuml` 之后、图内容之前。

### 常用内置主题

| 主题 | 风格 |
|------|------|
| `plain` | 简单黑底白字（默认风格对照） |
| `bluegray` | 蓝灰 |
| `blueprint` | 蓝图风格（白底蓝线，仿蓝图复印） |
| `amiga` | Amiga Workbench 1.x（白字蓝底） |
| `mimeograph` | 油印风格（灰底紫字） |
| `cyborg` / `superhero` / `united` / `minty` / `sandstone` / `sketchy` / `spacelab` / `materia` / `cerulean` | Bootswatch 风格系列 |
| `hacker` | Jekyll hacker 风格（终端感） |
| `crt-amber` | 单色 CRT 琥珀色（橙字黑底） |
| `reddress-darkblue` / `reddress-lightblue` | Red Dress 红裙风格（深/浅蓝） |
| `aws-orange` | AWS 配色 |
| `cloudscape-design` | Cloudscape 设计配色 |
| `carbon-gray` | Carbon 设计灰阶 |
| `Sunlust` | Solarized 配色 |
| `black-knight` / `metal` / `silver` / `lightgray` | 深色/金属/灰色系 |
| `mars` / `toy` / `vibrant` | future-architect/puml-themes 系列 |
| `mono` | 单色 + 等宽字体 |

> 部分主题（如 `cyborg`、`sketchy`、`reddress-*` 等）有多个变体，可在主题详情页查看。完整主题画廊与预览：
> <https://the-lum.github.io/puml-themes-gallery/themes/>

### 主题变体与使用

- 主题名区分大小写（如 `Sunlust`）。
- 可指定皮肤变体：`!theme cyborg-outline` 等（具体变体名参考画廊详情页）。
- 主题可叠加 `<style>` 进一步微调。
- 不确定用哪个时，可先选对照主题 `plain`，再按需切换。

### 主题 vs skinparam

- `!theme`：一键整套预设外观，优先使用。
- `skinparam`：细粒度参数覆盖（已废弃，仍可用），仅在主题基础上微调个别参数。
- `<style>`：CSS 式样（主题的底层实现），高级自定义推荐方式。

## 非 UML 图表

PlantUML 不仅能画 UML，还支持大量非 UML 图表类型。当用户需要画结构/数据/界面/流程类图表时，优先考虑用 PlantUML 表达。完整列表见 <https://plantuml.com/zh/>。

### 常用非 UML 图表语法

**JSON / YAML 数据**（数据结构可视化）
```
@startjson
{
  "name": "张三",
  "age": 30,
  "tags": ["a", "b"],
  "address": {"city": "北京"}
}
@endjson
```
```
@startyaml
name: 张三
age: 30
address:
  city: 北京
@endyaml
```

**WBS 分解图**（工作分解结构）
```
@startwbs
* 项目
** 阶段一
*** 任务A
*** 任务B
** 阶段二
@endwbs
```

**Salt 界面原型**（线框图）
```
@startsalt
{
  Login
  [用户名] [______]
  [密码]   [______]
  [  登录  ] [ 取消 ]
}
@endsalt
```

**ER 实体关系图**
```
@startuml
entity "用户" as user {
  * id : int
  * name : string
}
entity "订单" as order {
  * id : int
  * user_id : int
}
user ||--o{ order
@enduml
```

**网络图 (nwdiag)**
```
@startuml
nwdiag {
  network 内网 {
    server [address = "10.0.0.1"];
    db     [address = "10.0.0.2"];
  }
}
@enduml
```

**正则表达式图表**
```
@startregex
A|B(CD)*E
@endregex
```

**EBNF 语法图**
```
@startebnf
digit = "0" | "1" | ... ;
@endebnf
```

**Archimate 架构图**
```
@startuml
Archimate_BusinessFunction
Archimate_ApplicationComponent
@enduml
```

### 非 UML 图表类型清单

- 数据：JSON、YAML、EBNF、Regex、ER（实体关系）、信息工程图（IE）
- 结构：网络图（nwdiag）、架构图（Archimate）、WBS、Files（文件树）、Chart
- 界面：Salt（UI 线框模型）
- 流程：SDL、Ditaa、甘特图、时序图（chronology）
- 其他：AsciiMath / JLaTeXMath 数学公式

## skinparam 常用参数

> 注意：skinparam 已废弃，建议迁移到 `<style>` CSS 样式。

```
skinparam backgroundColor transparent
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Helvetica
skinparam classFontColor red
skinparam classFontSize 10
skinparam ArrowHeadColor none
skinparam componentStyle rectangle
```

嵌套写法：
```
skinparam class {
  FontColor red
  FontSize 10
  FontName Helvetica
}
```

## 预处理

### 变量

```
!$var = "value"
!$i = 42
!$a ?= "default"
```

### 条件

```
!if ($var == "value")
  ...
!else
  ...
!endif
```

### 循环

```
!while ($i > 0)
  ...
!endwhile
```

### 函数

```
!function $name($param)
  !return $param + "!"
!endfunction
```

### 包含文件

```
!include file.iuml
!include_many file.iuml
!include_once file.iuml
!includesub file.puml!SECTION
```

### 内置函数

`%date()`, `%now()`, `%darken("red", 20)`, `%chr(65)`, `%intval("42")`, `%file_exists("path")` 等。

## 颜色

支持标准颜色名（`red`, `blue`, `green` 等）和 RGB 码（`#FF0000`）。`transparent` 仅用于背景。

内联颜色样式：`#color;line:color;line.[bold|dashed|dotted];text:color`。

## 输出与渲染

- 命令行：`java -jar plantuml.jar file.puml`
- 输出格式：`-tpng`（默认）、`-tsvg`、`-tpdf`、`-tlatex`
- 服务器：可使用 PlantUML Web 服务器渲染
- `!pragma` 指令可控制渲染行为
