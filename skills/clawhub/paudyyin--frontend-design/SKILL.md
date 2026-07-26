---
name: frontend-design
version: 2.4.0
description: "Create distinctive, accessible frontend interfaces with deliberate palette, typography, and layout choices. Use when building UI components, pages, dashboards, or landing pages. Includes 73+ brand DESIGN.md references, HTML slide generation, design system token architecture, and shadcn/ui/Tailwind styling guides."
dependencies:
  node: []
  system:
    - Modern browser (Chrome/Firefox/Safari) for preview
    - Python 3.x (for design system generator)
---

# Frontend Design

Approach this as the design lead at a small studio known for giving every client a visual identity that could not be mistaken for anyone else's. This client has already rejected proposals that felt templated, and is paying for a distinctive point of view: make deliberate, opinionated choices about palette, typography, and layout that are specific to this brief, and take one real aesthetic risk you can justify.

---

## 0. Brief Inference (Read the Room First)

Before touching code or tweaking dials, **infer what the user actually wants**. Most LLM design output is bad because the model jumps to a default aesthetic instead of reading the room.

### 0.A Read These Signals First

1. **Page kind** - landing (SaaS / consumer / agency / event), portfolio (dev / designer / creative studio), redesign (preserve vs overhaul), editorial / blog, dashboard, internal tool.
2. **Vibe words** the user used - "minimalist", "calm", "Linear-style", "Awwwards", "brutalist", "premium consumer", "Apple-y", "playful", "serious B2B", "editorial", "agency-y", "glassy", "dark tech".
3. **Reference signals** - URLs they linked, screenshots they pasted, products they named, brands they're competing with.
4. **Audience** - B2B procurement panel vs. design-conscious consumer vs. recruiter scanning a portfolio. The audience picks the aesthetic, not your taste.
5. **Brand assets that already exist** - logo, color, type, photography. For redesigns, these are starting material, not optional input.
6. **Quiet constraints** - accessibility-first audiences, public-sector, regulated industries, trust-first commerce, kids' products. These constraints OVERRIDE aesthetic preference.

### 0.B Output a One-Line "Design Read" Before Generating

Before any code, state in one line: **"Reading this as: <page kind> for <audience>, with a <vibe> language, leaning toward <design system or aesthetic family>."**

Example reads:
- *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."*
- *"Reading this as: solo designer portfolio for hiring managers, with an editorial / kinetic-type language, leaning toward native CSS + scroll-driven animation + custom typography."*
- *"Reading this as: internal dashboard for logistics operators, with a trust-first utilitarian language, leaning toward Carbon Design + dense data tables."*

### 0.C If the Brief Is Ambiguous, Ask One Question

Ask exactly **one** clarifying question - never a multi-question dump - and only when the design read genuinely diverges. Example: *"Should this feel closer to Linear-clean or Awwwards-experimental?"*

If you can confidently infer from context, **do not ask**. Just declare the design read and proceed.

### 0.D Anti-Default Discipline

Do not default to: AI-purple gradients, centered hero over dark mesh, three equal feature cards, generic glassmorphism on everything, infinite-loop micro-animations everywhere, Inter + slate-900. These are the LLM defaults. Reach past them deliberately based on the design read.

See `references/anti-slop.md` for the complete anti-pattern checklist.

---

## 1. The Three Dials (Core Configuration)

After the design read, set three dials. Every layout, motion, and density decision below is gated by these.

* **`DESIGN_VARIANCE: 7`** - 1 = Perfect Symmetry, 10 = Artsy Chaos
* **`MOTION_INTENSITY: 5`** - 1 = Static, 10 = Cinematic / Physics
* **`VISUAL_DENSITY: 4`** - 1 = Art Gallery / Airy, 10 = Cockpit / Packed Data

### 完成条件

- **Step 0（Brief Inference）完成条�?*：已输出一�?Design Read"声明（page kind + audience + vibe + design system），且在模糊场景下最多问�?1 个澄清问题�?- **Step 1（Three Dials）完成条�?*：已设置 DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY 三个参数值，并说明选择理由�?- **整体完成条件**：已生成可预览的前端代码，配�?字体/布局均非 LLM 默认风格（非 purple gradients / dark mesh / glassmorphism），WCAG 2.1 AA 对比度检查通过，响应式断点（mobile/tablet/desktop）已覆盖�?
**Baseline:** `7 / 5 / 4`. Use these unless the design read overrides them.

### 1.A Dial Inference (Design Read �?Dial Values)

| Signal | VARIANCE | MOTION | DENSITY |
|--------|----------|--------|---------|
| "minimalist / clean / calm / editorial / Linear-style" | 5-6 | 3-4 | 2-3 |
| "premium consumer / Apple-y / luxury / brand" | 7-8 | 5-7 | 3-4 |
| "playful / wild / Dribbble / Awwwards / experimental / agency" | 9-10 | 8-10 | 3-4 |
| "landing page / portfolio / marketing site (default)" | 7-9 | 6-8 | 3-5 |
| "dashboard / internal tool / data-heavy" | 4-5 | 2-3 | 7-9 |
| "trust-first / public-sector / regulated / accessibility-critical" | 3-4 | 2-3 | 4-5 |
| "redesign - preserve" | match existing | +1 | match existing |
| "redesign - overhaul" | +2 | +2 | match existing |

### 1.B How the Dials Drive Output

Use these (or user-overridden values) as global variables. Cross-references throughout this document refer to these exact variable names.

---

## 2. Design System Selection

Once you have the design read (Section 0) and dials (Section 1), pick the right foundation. Do not invent CSS for things that have an official package.

### 2.A When to Reach for a Real Design System

| Brief reads as�?| Reach for | Why |
|-----------------|-----------|-----|
| Microsoft / enterprise SaaS / dashboards | `@fluentui/react-components` | Official Fluent UI, Microsoft tokens, accessibility done |
| Google-ish UI, Material-flavored product | `@material/web` + Material 3 tokens | Official, theme-able via Material Theming |
| IBM-style B2B / enterprise analytics | `@carbon/react` + `@carbon/styles` | Official Carbon, mature data-density patterns |
| Shopify app surfaces | `polaris.js` web components / Polaris React | Required for Shopify admin UI |
| Atlassian / Jira-style product | `@atlaskit/*` + `@atlaskit/tokens` | Official Atlassian DS |
| GitHub-style devtool / community page | `@primer/css` or `@primer/react-brand` | Official Primer; Brand variant for marketing |
| Public-sector UK service | `govuk-frontend` | Legally / regulatorily expected |
| US public-sector / trust-first | `uswds` | Same |
| Modern accessible React foundation | `@radix-ui/themes` | Primitives + polished theme |
| Modern SaaS where you own the components | shadcn/ui (`npx shadcn@latest add ...`) | You own the code, easy to customise |
| Tailwind-based modern SaaS / AI marketing | Tailwind v4 utilities + `dark:` variant | Default for indie + small team builds |

**Honesty rule:** if the brief reads as one of the systems above, install and use the **official** package. Do not recreate its CSS by hand.

**One system per project.** Do not mix Fluent React with Carbon in the same tree.

### 2.B When the Brief Is an Aesthetic, Not a System

For these directions, there is **no single official package**. Build with native CSS + Tailwind + a maintained component library.

| Aesthetic | Honest implementation |
|-----------|----------------------|
| Glassmorphism / "frosted glass" | `backdrop-filter`, layered borders, highlight overlays. Provide solid-fill fallback for `prefers-reduced-transparency`. |
| Bento (Apple-style tile grids) | CSS Grid with mixed cell sizes. No single library owns this. |
| Brutalism | Native CSS, monospace, raw borders. No library. |
| Editorial / magazine | Serif type, asymmetric grid, generous whitespace. No library. |
| Dark tech / hacker | Mono + accent neon, terminal motifs. No library. |
| Aurora / mesh gradients | SVG or layered radial gradients. No library. |

See `references/design-systems.md` for detailed implementation guidance.

---

## 2.C Brand Design Reference (v2.3 新增)

When the user references a specific brand style (e.g., "Linear 风格", "Vercel 风格", "美的风格"), 
load the corresponding `DESIGN.md` from the local collection:

**Path**: `references/design-md-collection/<brand>/DESIGN.md`

### Available Brands (73 + custom)

| Category | Brands |
|----------|--------|
| AI & LLM | Claude, Cohere, ElevenLabs, Minimax, Mistral AI, Ollama, OpenCode AI, Replicate, Runway, Together AI, VoltAgent, xAI |
| Dev Tools | Cursor, Expo, Lovable, Raycast, Superhuman, Vercel, Warp |
| Data & Infra | ClickHouse, Composio, HashiCorp, MongoDB, PostHog, Sentry, Supabase |
| SaaS | Cal.com, Intercom, Linear, Mintlify, Notion, Resend, Zapier, Airtable, Clay, Figma, Framer, Miro, Webflow |
| Fintech | Binance, Coinbase, Kraken, Mastercard, Revolut, Stripe, Wise |
| Retail | Airbnb, Meta, Nike, Shopify, Starbucks, Apple, HP, IBM, NVIDIA, Pinterest, PlayStation, SpaceX, Spotify, The Verge, Uber, Vodafone, WIRED |
| Auto | BMW, BMW M, Bugatti, Ferrari, Lamborghini, Renault, Tesla |
| **Custom** | **midea-wcs** (美的智能装备所 WCS 系统) |

### How to Use

1. **User says "像 Linear 那种风格"** → read `references/design-md-collection/linear.app/DESIGN.md`
2. **User says "WCS 系统加个页面"** → read `references/design-md-collection/midea-wcs/DESIGN.md`
3. **Use the DESIGN.md tokens** (colors, typography, spacing, components) as the **primary design system**
4. **Merge with Section 1 dials**: if the DESIGN.md specifies a style, adjust dials accordingly

### Priority Order

1. User explicitly names a brand → load that brand's DESIGN.md
2. Brief maps to a known brand style → load that DESIGN.md and declare the match
3. No brand reference → use Section 2.A/B selection as before

**Honesty rule**: the DESIGN.md provides tokens and patterns, not rules. Override when the brief conflicts.

---

## 3. Ground It in the Subject

If the brief does not pin down what the product or subject is, pin it yourself before designing: name one concrete subject, its audience, and the page's single job, and state your choice. If there's any information in your memory about the human's preferences, context about what they're building, or designs you've made before �?use that as a hint. The subject's own world, its materials, instruments, artifacts, and vernacular, is where distinctive choices come from. Build with the brief's real content and subject matter throughout.

## 4. Design Principles

For web designs, the hero is a thesis. Open with the most characteristic thing in the subject's world, in whatever form makes sense for it: a headline, an image, an animation, a live demo, an interactive moment. Be deliberate with your choice: a big number with a small label, supporting stats, and a gradient accent is the template answer, only use if that's truly the best option.

Typography carries the personality of the page. Pair the display and body faces deliberately, not the same families you would reach for on any other project, and set a clear type scale with intentional weights, widths, and spacing. Make the type treatment itself a memorable part of the design, not a neutral delivery vehicle for the content.

Structure is information. Structural devices, numbering, eyebrows, dividers, labels, should encode something true about the content, not decorate it. Many generic designs use numbered markers (01 / 02 / 03), but that's only appropriate if the content actually is a sequence - like a real process or a typed timeline where order carries information the reader needs. Question if choices like numbered markers actually make sense before incorporating them.

Leverage motion deliberately. Think about where and if animation can serve the subject: a page-load sequence, a scroll-triggered reveal, hover micro-interactions, ambient atmosphere. An orchestrated moment usually lands harder than scattered effects; choose what the direction calls for. However, sometimes less is more, and extra animation contributes to the feeling that the design is AI-generated.

Match complexity to the vision. Maximalist directions need elaborate execution; minimal directions need precision in spacing, type, and detail. Elegance is executing the chosen vision well.

Consider written content carefully. Often a design brief may not contain real content, and it's up to you to come up with copy. Copy can make a design feel as templated as the design itself. See the below section on writing for more guidance.

## 5. Process: Brainstorm, Explore, Plan, Critique, Build, Critique Again

For calibration: AI-generated design right now clusters around three looks: (1) a warm cream background (near #F4F1EA) with a high-contrast serif display and a terracotta accent; (2) a near-black background with a single bright acid-green or vermilion accent; (3) a broadsheet-style layout with hairline rules, zero border-radius, and dense newspaper-like columns. All three are legitimate for some briefs, but they are defaults rather than choices, and they appear regardless of subject. Where the brief pins down a visual direction, follow it exactly �?the brief's own words always win, including when it asks for one of these looks. Where it leaves an axis free, don't spend that freedom on one of these defaults. Just like a human designer who's hired, there's often a careful balance between doing what you're good at and taking each project as a chance to experiment and learn.

Work in two passes. First, brainstorm a short design plan based on the human's design brief: create a compact token system with color, type, layout, and signature. Color: describe the palette as 4�? named hex values. Type: the typefaces for 2+ roles (a characterful display face that's used with restraint, a complementary body face, and a utility face for captions or data if needed). Layout: a layout concept, using one-sentence prose descriptions and ASCII wireframes to ideate and compare. Signature: the single unique element this page will be remembered by that embodies the brief in an appropriate way.

Then review that plan against the brief before building: if any part of it reads like the generic default you would produce for any similar page (work through a similar prompt to see if you arrive somewhere similar) rather than a choice made for this specific brief �?revise that part, say what you changed and why. Only after you've confirmed the relative uniqueness of your design plan should you start to write the code, following the revised plan exactly and deriving every color and type decision from it.

When writing the code, be careful of structuring your CSS selector specificities. It's easy to generate CSS classes that cancel each other out (especially with a type-based selector like .section and a element-based selector like .cta). This can happen often with paddings/margins between sections.

Try to do a lot of this planning and iteration in your thinking, and only show ideas to the user when you have higher confidence it'll delight them.

## 6. Restraint and Self-Critique

Spend your boldness in one place. Let the signature element be the one memorable thing, keep everything around it quiet and disciplined, and cut any decoration that does not serve the brief. Not taking a risk can be a risk itself! Build to a quality floor without announcing it: responsive down to mobile, visible keyboard focus, reduced motion respected. Critique your own work as you build, taking screenshots if your environment supports it �?a picture is worth 1000 tokens. Consider Chanel's advice: before leaving the house, take a look in the mirror and remove one accessory. Human creators have memory and always try to do something new, so if you have a space to quickly jot down notes about what you've tried, it can help you in future passes.

## 7. More on Writing in Design

Words appear in a design for one reason: to make it easier to understand, and therefore easier to use. They are design material, not decoration. Bring the same intentionality to copy that you would bring to spacing and color. Before writing anything, ask what the design needs to say, and how it can best be said to help the person navigate the experience.

Write from the end user's side of the screen. Name things by what people control and recognize, never by how the system is built. A person manages notifications, not webhook config. Describe what something does in plain terms rather than selling it. Being specific is always better than being clever.

Use active voice as default. A control should say exactly what happens when it's used: "Save changes," not "Submit." An action keeps the same name through the whole flow, so the button that says "Publish" produces a toast that says "Published." The vocabulary of an interface is the signposting for someone navigating the product. Cohesion and consistency are how people learn their way around.

Treat failure and emptiness as moments for direction, not mood. Explain what went wrong and how to fix it, in the interface's voice rather than a person's. Errors don't apologize, and they are never vague about what happened. An empty screen is an invitation to act.

Keep the register conversational and tuned: plain verbs, sentence case, no filler, with tone matched to the brand and the audience. Let each element do exactly one job. A label labels, an example demonstrates, and nothing quietly does double duty.

---

## 8. Pre-Output Checklist

Before delivering, verify:

### Design Read & Dials
- [ ] Output a one-line "Design Read" before generating code
- [ ] Set three dials (DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY) based on the brief
- [ ] Selected appropriate design system or aesthetic family

### Anti-Slop Verification
- [ ] No banned fonts (Inter/Roboto as display, Fraunces, Instrument_Serif)
- [ ] No AI-default purple gradients
- [ ] No centered hero with three equal cards
- [ ] No generic glassmorphism without justification
- [ ] No placeholder content (Lorem ipsum, "Acme Corp", "John Doe")

### Quality Floor
- [ ] Color palette has 4-6 named hex values, not just "primary/secondary"
- [ ] Typography has at least 2 distinct faces (display + body)
- [ ] Layout has a clear visual hierarchy (what's the hero?)
- [ ] There's one signature element that makes this memorable
- [ ] Copy is written from user's perspective, not system's
- [ ] Responsive down to mobile viewport (test: 320px, 768px, 1024px, 1440px)
- [ ] Focus states visible for keyboard navigation
- [ ] Reduced motion respected (prefers-reduced-motion)

### Accessibility (WCAG 2.1 AA)
- [ ] All interactive elements keyboard accessible (Tab through the page)
- [ ] ARIA labels on icon-only buttons and inputs without visible labels
- [ ] Focus management: dialog traps focus, content changes move focus
- [ ] Color contrast: 4.5:1 normal text, 3:1 large text
- [ ] Color is not the sole indicator of state (use icons/text too)
- [ ] Loading, error, and empty states all handled (no blank screens)

### Technical
- [ ] CSS selector specificities are consistent
- [ ] No layout-triggering animation properties (use transform/opacity)
- [ ] `min-h-[100dvh]` instead of `h-screen` for full-height sections
- [ ] CSS Grid instead of complex flexbox percentage math
- [ ] All imports verified in package.json
- [ ] Spacing uses consistent scale (no arbitrary pixel values)
- [ ] Semantic color tokens (text-primary, bg-surface) not raw hex in components
- [ ] Components < 200 lines each (split if larger)

---

## 9. Error Handling

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| CSS classes cancel each other out | Selector specificity conflicts | Use consistent class naming, avoid mixing type and class selectors |
| Fonts not loading | External font CDN blocked | Use system font stack as fallback, or self-host fonts |
| Layout breaks on mobile | Fixed pixel values | Use relative units (rem, em, vw/vh) and media queries |
| Animation jank | Too many simultaneous animations | Reduce animation count, use CSS transforms instead of layout properties |
| Dark mode colors look wrong | Direct color inversion | Use HSL color space for better control, test both modes |

### Graceful Degradation

```
Feature support priority:
1. Core layout and content �?Always works (even without JS)
2. Visual styling �?Degrades gracefully on older browsers
3. Animations and interactions �?Respect prefers-reduced-motion
4. Advanced CSS features �?Provide fallbacks for grid/subgrid
```

### Browser Compatibility

- **Target**: Last 2 versions of Chrome, Firefox, Safari, Edge
- **Fallbacks**: Use `@supports` for advanced CSS features
- **Testing**: Preview in at least 2 browsers before delivery

---

## 10. Data-Driven Design System Generator (v2.1 新增)

> 基于 UI UX Pro Max v2.0 �?CSV 数据库，提供数据驱动的设计系统推荐�?
### 10.1 数据库规�?
| 数据文件 | 大小 | 内容 |
|----------|------|------|
| `data/design.csv` | 106KB | 核心设计规则�?|
| `data/styles.csv` | 143KB | 67种UI风格详细定义 |
| `data/colors.csv` | 32KB | 161个行业调色板 |
| `data/products.csv` | 58KB | 161种产品类型推理规�?|
| `data/typography.csv` | 50KB | 57组字体配�?|
| `data/charts.csv` | 19KB | 25种图表推�?|
| `data/ux-guidelines.csv` | 19KB | 99条UX准则 |
| `data/motion.csv` | 11KB | GSAP动画片段 |
| `data/icons.csv` | 21KB | 图标库推�?|
| `data/google-fonts.csv` | 743KB | Google Fonts完整目录 |
| `data/landing.csv` | 17KB | 24种落地页模式 |
| `data/app-interface.csv` | 10KB | 应用界面模式 |
| `data/react-performance.csv` | 15KB | React性能准则 |

### 10.2 使用方式

#### 搜索特定领域

```bash
# 搜索颜色方案
python scripts/search.py "SaaS dashboard" --domain color

# 搜索字体配对
python scripts/search.py "elegant luxury" --domain typography

# 搜索UX准则
python scripts/search.py "touch target" --domain ux

# 搜索图表推荐
python scripts/search.py "trend time-series" --domain chart

# 搜索UI风格
python scripts/search.py "glassmorphism" --domain style
```

#### 生成完整设计系统

```bash
# 生成设计系统推荐
python scripts/search.py "beauty spa landing page" --design-system -p "Serenity Spa"

# 带设计旋�?python scripts/search.py "fintech dashboard" --design-system --variance 6 --motion 4 --density 8

# 持久化到文件（Master + Pages 模式�?python scripts/search.py "e-commerce mobile" --design-system --persist -p "ShopFlow"

# 创建页面级覆�?python scripts/search.py "product detail page" --design-system --persist -p "ShopFlow" --page "product-detail"
```

#### 技术栈特定搜索

```bash
# React 性能准则
python scripts/search.py "re-render" --stack react

# SwiftUI 指南
python scripts/search.py "navigation" --stack swiftui

# Tailwind + shadcn/ui
python scripts/search.py "dark mode" --stack shadcn
```

**支持的技术栈**：react, nextjs, vue, svelte, astro, swiftui, react-native, flutter, nuxtjs, nuxt-ui, html-tailwind, shadcn, jetpack-compose, threejs, angular, laravel, javafx, wpf, winui, avalonia, uno, uwp

### 10.3 设计系统输出结构

```
┌─────────────────────────────────────────────────────────────────�?�? TARGET: <Project Name> - RECOMMENDED DESIGN SYSTEM             �?├─────────────────────────────────────────────────────────────────�?�? PATTERN: <Landing Page Pattern Name>                           �?�?    Conversion: <策略>                                          �?�?    CTA: <位置>                                                 �?�?    Sections: <章节顺序>                                        �?├─────────────────────────────────────────────────────────────────�?�? STYLE: <UI Style Name>                                         �?�?    Keywords: <关键�?                                          �?�?    Best For: <适用场景>                                        �?�?    Performance: <评级> | Accessibility: <评级>                 �?├─────────────────────────────────────────────────────────────────�?�? COLORS:                                                        �?�?    Primary:    #XXXXXX (--color-primary)                       �?�?    Secondary:  #XXXXXX (--color-secondary)                     �?�?    Accent/CTA: #XXXXXX (--color-accent)                        �?�?    Background: #XXXXXX (--color-background)                    �?�?    Foreground: #XXXXXX (--color-foreground)                    �?�?    Notes: <配色说明>                                           �?├─────────────────────────────────────────────────────────────────�?�? TYPOGRAPHY: <Heading Font> / <Body Font>                       �?�?    Mood: <字体情绪>                                            �?�?    Google Fonts: <URL>                                         �?�?    CSS Import: <代码>                                          �?├─────────────────────────────────────────────────────────────────�?�? KEY EFFECTS: <关键效果>                                        �?├─────────────────────────────────────────────────────────────────�?�? AVOID (Anti-patterns): <反模�?                                �?├─────────────────────────────────────────────────────────────────�?�? PRE-DELIVERY CHECKLIST:                                        �?�?    [ ] No emojis as icons (use SVG: Heroicons/Lucide)          �?�?    [ ] cursor-pointer on all clickable elements                �?�?    [ ] Hover states with smooth transitions (150-300ms)        �?�?    [ ] Light mode: text contrast 4.5:1 minimum                 �?�?    [ ] Focus states visible for keyboard nav                   �?�?    [ ] prefers-reduced-motion respected                        �?�?    [ ] Responsive: 375px, 768px, 1024px, 1440px               �?└─────────────────────────────────────────────────────────────────�?```

### 10.4 持久化模式（Master + Overrides�?
使用 `--persist` 参数将设计系统保存到文件�?
```
design-system/<project-slug>/
├── MASTER.md              # 全局设计源（Global Source of Truth�?└── pages/                 # 页面级覆�?    ├── dashboard.md
    ├── product-detail.md
    └── settings.md
```

**规则**：页面级文件覆盖 MASTER.md 中的同名规则。构建页面时先检�?pages/ 目录�?
### 10.5 10优先�?UX 检查清�?
生成 UI 代码后，按优先级依次检查：

1. **无障�?* (CRITICAL) - 对比�?.5:1, 键盘导航, Aria标签
2. **触摸交互** (CRITICAL) - 最�?4×44px, 8px间距
3. **性能** (HIGH) - WebP/AVIF, 懒加�? CLS<0.1
4. **风格选择** (HIGH) - 匹配产品类型, SVG图标
5. **布局响应�?* (HIGH) - 移动优先, 无水平滚�?6. **排版色彩** (MEDIUM) - 基准16px, 语义化token
7. **动画** (MEDIUM) - 150-300ms, 有意义运�?8. **表单反馈** (MEDIUM) - 可见标签, 错误就近
9. **导航模式** (HIGH) - 可预测返�? 底部导航�?
10. **图表数据** (LOW) - 图例, 工具提示

详见 `references/ux-priorities.md`

---

## 11. Style Variants

For specific aesthetic directions, see the `ui-styles` skill:
- **soft** - High-end, calm, expensive UI with softer contrast and spring motion
- **minimalist** - Editorial product UI (Notion/Linear vibes), restrained palette
- **brutalist** - Hard mechanical language: Swiss type, sharp contrast, experimental layout

---

## 12. UI Engineering (v2.2 新增)

> 来源：Anthropic 官方 frontend-ui-engineering skill。设计规范决�?长什么样"，工程规范决�?怎么�?�?
### 12.1 Component Architecture

**文件共置**：组件相关的一切放在一起�?
```
src/components/
  TaskList/
    TaskList.tsx          # 组件实现
    TaskList.test.tsx     # 测试
    TaskList.stories.tsx  # Storybook（可选）
    use-task-list.ts      # 自定�?hook（复杂状态时�?    types.ts              # 组件类型（需要时�?```

**组合优于配置**�?
```tsx
// �?组合�?<Card>
  <CardHeader><CardTitle>Tasks</CardTitle></CardHeader>
  <CardBody><TaskList tasks={tasks} /></CardBody>
</Card>

// �?过度配置
<Card title="Tasks" headerVariant="large" bodyPadding="md" content={<TaskList tasks={tasks} />} />
```

**容器/展示分离**�?
```tsx
// 容器：处理数�?export function TaskListContainer() {
  const { tasks, isLoading, error } = useTasks();
  if (isLoading) return <TaskListSkeleton />;
  if (error) return <ErrorState message="Failed to load tasks" retry={refetch} />;
  if (tasks.length === 0) return <EmptyState message="No tasks yet" />;
  return <TaskList tasks={tasks} />;
}

// 展示：处理渲�?export function TaskList({ tasks }: { tasks: Task[] }) {
  return <ul role="list" className="divide-y">{tasks.map(task => <TaskItem key={task.id} task={task} />)}</ul>;
}
```

### 12.2 State Management

**选择最简方案**�?
```
Local state (useState)           �?组件专属 UI 状�?Lifted state                     �?2-3 个兄弟组件共�?Context                          �?主题/认证/语言（读多写少）
URL state (searchParams)         �?筛�?分页/可分享状�?Server state (React Query/SWR)   �?远程数据+缓存
Global store (Zustand/Redux)     �?全应用共享的复杂客户端状�?```

**Prop drilling 不超�?3 层�?* 超过时引�?context 或重构组件树�?
### 12.3 Accessibility (WCAG 2.1 AA)

**键盘导航**�?
```tsx
// �?可聚�?<button onClick={handleClick}>Click me</button>

// �?不可聚焦
<div onClick={handleClick}>Click me</div>

// �?但优先用 <button>
<div role="button" tabIndex={0} onClick={handleClick}
     onKeyDown={e => { if (e.key === 'Enter') handleClick(); if (e.key === ' ') e.preventDefault(); }}
     onKeyUp={e => { if (e.key === ' ') handleClick(); }}>
  Click me
</div>
```

**ARIA 标签**�?
```tsx
<button aria-label="Close dialog"><XIcon /></button>
<label htmlFor="email">Email</label>
<input id="email" type="email" />
<input aria-label="Search tasks" type="search" />
```

**焦点管理**�?
```tsx
function Dialog({ isOpen, onClose }: DialogProps) {
  const closeRef = useRef<HTMLButtonElement>(null);
  useEffect(() => { if (isOpen) closeRef.current?.focus(); }, [isOpen]);
  return (
    <dialog open={isOpen}>
      <button ref={closeRef} onClick={onClose}>Close</button>
      {/* dialog content */}
    </dialog>
  );
}
```

**空状态和错误状�?*（不要显示空白屏幕）�?
```tsx
function TaskList({ tasks }: { tasks: Task[] }) {
  if (tasks.length === 0) {
    return (
      <div role="status" className="text-center py-12">
        <TasksEmptyIcon className="mx-auto h-12 w-12 text-muted" />
        <h3 className="mt-2 text-sm font-medium">No tasks</h3>
        <p className="mt-1 text-sm text-muted">Get started by creating a new task.</p>
        <Button className="mt-4" onClick={onCreateTask}>Create Task</Button>
      </div>
    );
  }
  return <ul role="list">...</ul>;
}
```

### 12.4 Responsive Design

**Mobile-first**�?
```tsx
<div className="
  grid grid-cols-1      /* Mobile: single column */
  sm:grid-cols-2        /* Small: 2 columns */
  lg:grid-cols-3        /* Large: 3 columns */
  gap-4
">
```

**测试断点**�?20px, 768px, 1024px, 1440px

### 12.5 Loading & Transitions

**Skeleton 加载**（不要用 spinner）：

```tsx
function TaskListSkeleton() {
  return (
    <div className="space-y-3" aria-busy="true" aria-label="Loading tasks">
      {Array.from({ length: 3 }).map((_, i) => (
        <div key={i} className="h-12 bg-muted animate-pulse rounded" />
      ))}
    </div>
  );
}
```

**乐观更新**（感知速度）：

```tsx
function useToggleTask() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: toggleTask,
    onMutate: async (taskId) => {
      await queryClient.cancelQueries({ queryKey: ['tasks'] });
      const previous = queryClient.getQueryData(['tasks']);
      queryClient.setQueryData(['tasks'], (old: Task[]) =>
        old.map(t => t.id === taskId ? { ...t, done: !t.done } : t)
      );
      return { previous };
    },
    onError: (_err, _taskId, context) => {
      queryClient.setQueryData(['tasks'], context?.previous);
    },
  });
}
```

### 12.6 Spacing & Typography Rules

**间距**：使用一致的间距刻度，不发明任意值�?
```css
/* �?在刻度上 */  padding: 1rem;      /* 16px = 4×4px */
/* �?在刻度上 */  gap: 0.75rem;       /* 12px = 3×4px */
/* �?不在刻度 */  padding: 13px;
/* �?不在刻度 */  margin-top: 2.3rem;
```

**排版层级**：不跳级，不用标题样式做非标题内容�?
```
h1 �?页面标题（每页一个）
h2 �?区块标题
h3 �?子区块标�?body �?默认文本
small �?辅助/说明文本
```

**颜色**：用语义�?token（`text-primary`, `bg-surface`, `border-default`），不用�?hex。对比度：正�?4.5:1，大文本 3:1。不单独靠颜色传达信息�?
### 12.7 Red Flags

- 组件超过 200 行（拆分�?- 内联样式或任意像素�?- 缺少错误/加载/空状�?- 没有测试键盘导航
- 用颜色作为唯一状态指示器（红/绿没有文字或图标�?- 通用 "AI 外观"（紫色渐变、超大卡片、模板布局�?
### 12.8 Common Rationalizations

| 借口 | 现实 |
|------|------|
| "可访问性以后再�? | 很多地区是法律要求，也是工程质量标准 |
| "响应式以后再�? | 改造响应式比从头建�?3 �?|
| "设计没定稿，先不写样�? | 用设计系统默认值，未样式化�?UI 给审核者留下破碎印�?|
| "这只是原�? | 原型会变成生产代码，基础要建�?|
| "AI 外观先用着" | 它传递低质量感，从一开始就用项目的设计系统 |

---

## 13. Reference Resources (v2.4 新增)

This section indexes all reference materials available under eferences/. Load on demand — do not preload all files.

### 13.A Brand Design MD Collection (73+1 brands)

**Path**: eferences/design-md-collection/<brand>/DESIGN.md

Full brand design systems extracted from real websites. Each file contains color tokens, typography scales, spacing, component specs, patterns, and interaction guidelines.

**Key brands for our context**:
- midea-wcs — Midea Smart Manufacturing WCS (美的蓝 #0092D8, 微软雅黑, AGV fleet dashboard patterns)
- linear.app — Near-black + lavender accent, ultra-precise software craft aesthetic
- ercel — White canvas + mesh gradients, developer platform precision
- stripe — Purple gradients + weight-300 elegance, payment infrastructure
- supabase — Dark emerald, code-first developer tools
- cursor — Warm cream canvas + orange accent, AI-first code editor

**Usage**: See Section 2.C Brand Design Reference for routing logic.

### 13.B Slides — HTML Presentation Generation

**Path**: eferences/slides/

Generate presentation-quality HTML slides with Chart.js data visualization. Output is a self-contained HTML file — preview in browser, share as link, or screenshot for embedding.

**References**:
- eferences/slides/SKILL.md — Main slide generation skill
- eferences/slides/references/create.md — Slide creation patterns
- eferences/slides/references/html-template.md — HTML slide template structure
- eferences/slides/references/layout-patterns.md — Layout patterns for slides
- eferences/slides/references/slide-strategies.md — Presentation strategies
- eferences/slides/references/copywriting-formulas.md — Copywriting formulas for slides

**Use when**: Creating reports, quarterly reviews, project status updates, or any presentation where HTML format is preferred over PPTX.

### 13.C Design System Token Architecture

**Path**: eferences/design-system/

Three-layer token system (primitive → semantic → component) for systematic design-to-code handoff.

**References**:
- eferences/design-system/token-architecture.md — Token layer structure
- eferences/design-system/primitive-tokens.md — Raw design values
- eferences/design-system/semantic-tokens.md — Purpose-named aliases
- eferences/design-system/component-tokens.md — Component-specific tokens
- eferences/design-system/component-specs.md — Component state tables
- eferences/design-system/states-and-variants.md — Hover/active/disabled states
- eferences/design-system/tailwind-integration.md — Tailwind theme mapping

**Use when**: Building a new design system, creating CSS variable architecture, or integrating design tokens with Tailwind.

### 13.D UI Styling — shadcn/ui + Tailwind

**Path**: eferences/ui-styling/

Practical guides for building UI with shadcn/ui components and Tailwind CSS utilities.

**References**:
- eferences/ui-styling/shadcn-components.md — shadcn/ui component library
- eferences/ui-styling/shadcn-theming.md — shadcn/ui theme configuration
- eferences/ui-styling/shadcn-accessibility.md — Accessibility patterns
- eferences/ui-styling/tailwind-customization.md — Tailwind customization
- eferences/ui-styling/tailwind-responsive.md — Responsive design with Tailwind
- eferences/ui-styling/tailwind-utilities.md — Utility-first patterns
- eferences/ui-styling/canvas-design-system.md — Canvas-based visual design

**Use when**: Building React/Vue interfaces with shadcn/ui, customizing Tailwind themes, or implementing responsive layouts.

### 13.E Brand Guidelines Reference

**Path**: eferences/brand/

- eferences/brand/color-palette-management.md — Color system hierarchy (primary → secondary → neutral → semantic)
- eferences/brand/consistency-checklist.md — Pre-delivery brand consistency audit
- eferences/brand/typography-specifications.md — Typography methodology (scale ratios, responsive sizing, letter-spacing)

**Use when**: Defining a new brand color system, auditing visual consistency, or designing typography scales.

### 13.F Design Patterns (Logo, CIP, Banner, Icon)

**Path**: eferences/design/

- Logo design (55 styles, 30 palettes, 25 industry guides)
- Corporate Identity Program (50 deliverable types)
- Banner design (22 styles for social/ads/web/print)
- Icon design (15 styles, SVG generation)
- Social photo generation (multi-platform)

**References**:
- eferences/design/logo-design.md
- eferences/design/logo-color-psychology.md
- eferences/design/logo-style-guide.md
- eferences/design/cip-design.md
- eferences/design/banner-sizes-and-styles.md
- eferences/design/icon-design.md
- eferences/design/social-photos-design.md
- eferences/design/design-routing.md

**Use when**: Creating logos, brand identity materials, social media banners, or icon sets.

### 13.G Offline Font Library

**Path**: eferences/fonts/

30+ open-source .ttf font files for canvas-based visual design. No CDN required.

Includes: Arsenal SC, Big Shoulders, Boldonse, Bricolage Grotesque, Crimson Pro, DM Mono, Erica One, Geist Mono, Gloock, IBM Plex Mono/Serif, Instrument Sans/Serif, Italiana, JetBrains Mono, Jura, Libre Baskerville, Lora, National Park, Nothing You Could Do, Outfit, Pixelify Sans, Poiret One, Red Hat Mono, Silkscreen, Smooch Sans, Tektur, Work Sans, Young Serif.

**Use when**: Generating posters, banners, or visual compositions that require specific display fonts without network access.

---

*Version 2.4.0 - 整合 ui-ux-pro-max-skill 完整资源库：+73 品牌 DESIGN.md 参考库 + HTML 幻灯片生成 + 设计系统 Token 架构 + shadcn/ui + Tailwind 指南 + 品牌规范参考 + Logo/CIP/Banner/Icon 设计模式 + 离线字体库。新增 Section 13 索引全部参考资源。*