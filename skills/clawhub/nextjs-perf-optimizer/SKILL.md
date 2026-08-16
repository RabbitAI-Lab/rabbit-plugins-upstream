---
name: nextjs-performance-optimizer
version: "1.0.0"
category: frontend
tags:
  - nextjs
  - performance
  - core-web-vitals
  - lighthouse
  - optimization
  - react
  - ssr
  - bundle-size
  - web-vitals
  - speed
model: claude-sonnet-4-20250514
trigger_keywords:
  - Next.js performance
  - Core Web Vitals
  - Lighthouse score
  - LCP
  - CLS
  - INP
  - bundle size
  - page speed
  - optimization
  - React performance
pricing: "$9.99 one-time"
---

# Next.js Performance Optimizer

> **Audit and optimize Next.js applications for Core Web Vitals, bundle size, and runtime performance.** Detects LCP/CLS/INP issues, unnecessary client-side JavaScript, missing image optimization, and database query N+1s — outputs specific code fixes with projected improvements.

## Why This Skill Exists

Next.js performance issues are rarely about one thing — they compound: oversized bundles slow TTFB, client-side rendering hurts LCP, unoptimized images tank CLS, and heavy re-renders spike INP. This skill systematically audits each layer and provides copy-paste fixes.

## When to Activate

Activate when the user:
- Asks to improve Next.js performance or page speed
- Mentions Core Web Vitals, Lighthouse, LCP, CLS, or INP
- Has a slow Next.js app or poor Lighthouse scores
- Wants to reduce bundle size or optimize rendering
- Says "my Next.js app is slow" or "optimize this page"

## Workflow

### Step 1: Audit Core Web Vitals

Analyze each metric and identify root causes:

#### LCP (Largest Contentful Paint) — Target: <2.5s
| Common Cause | Detection Method | Fix |
|--------------|-----------------|-----|
| Large hero image unoptimized | Check `<img>` vs `next/image` | Switch to `next/image` with `priority` |
| Slow server response (TTFB) | Check `getServerSideProps`/RSC query time | Move to SSG or add caching |
| Render-blocking JS/CSS | Check `_app.tsx` imports | Use `dynamic()` for below-fold components |
| Web font loading | Check `@font-face` usage | Use `next/font` with `display: swap` |
| Client-side data fetching | Check `useEffect` + fetch on mount | Move to Server Component or `getStaticProps` |

#### CLS (Cumulative Layout Shift) — Target: <0.1
| Common Cause | Detection Method | Fix |
|--------------|-----------------|-----|
| Images without dimensions | Check `<img>` without width/height | Add `width` and `height` or use `next/image` |
| Dynamic content injection | Check for ads/embeds loading late | Reserve space with `min-height` |
| Web fonts causing reflow | Check FOIT/FOUT behavior | Use `next/font` or `size-adjust` |
| Async hydration | Check `next/dynamic` without `ssr: false` | Add loading skeleton with fixed dimensions |

#### INP (Interaction to Next Paint) — Target: <200ms
| Common Cause | Detection Method | Fix |
|--------------|-----------------|-----|
| Heavy event handlers | Check onClick with expensive logic | Debounce/throttle, use `startTransition` |
| Expensive re-renders | Check component tree without `memo` | Add `React.memo`, `useMemo`, `useCallback` |
| Synchronous layout calculations | Check `useLayoutEffect` usage | Use `useEffect` instead |
| Large client-side state | Check context with frequent updates | Split context, use `useSyncExternalStore` |

### Step 2: Bundle Size Analysis

Scan all imports and identify:

```markdown
## Bundle Analysis

### Server Components vs Client Components
| File | Type | Issue | Fix |
|------|------|-------|-----|
| app/page.tsx | Server ✅ | — | — |
| components/Chart.tsx | Client ⚠️ | `"use client"` but only uses d3 | Split: data fetch in Server, render in Client |
| components/Header.tsx | Client ⚠️ | Entire header is client for theme toggle | Split: only toggle button is client |

### Heavy Dependencies
| Package | Bundle Size | Used Features | Alternative | Saving |
|---------|------------|---------------|------------|--------|
| moment.js | 67KB | format, parse | date-fns (tree-shakeable) | 60KB |
| lodash | 72KB | get, debounce | es-toolkit | 65KB |
| chart.js | 200KB | line chart only | visx or lightweight-charts | 150KB |

### Dynamic Import Opportunities
| Component | Current | Recommendation | Saving |
|-----------|---------|---------------|--------|
| Dashboard | Static import | `dynamic(() => import('./Dashboard'), { ssr: false })` | 45KB from initial |
| RichEditor | Static import | `dynamic(() => import('./RichEditor'), { loading: () => <Skeleton /> })` | 80KB from initial |
| Charts | Static import | `dynamic(() => import('./Charts'))` | 200KB from initial |
```

### Step 3: Rendering Strategy Audit

Check each page route for optimal rendering strategy:

| Route | Current | Recommendation | Reason |
|-------|---------|---------------|--------|
| `/` (homepage) | SSR | SSG + ISR (revalidate: 3600) | Content changes hourly, not per-request |
| `/blog/[slug]` | SSR | SSG + ISR (revalidate: 86400) | Blog posts change rarely |
| `/dashboard` | SSR | Server Component + Client Islands | Auth check on server, interactivity on client |
| `/api/products` | Route Handler | Edge Runtime | No DB access needed, use external API |
| `/pricing` | SSR | SSG | Pricing rarely changes |

### Step 4: Image Optimization Audit

```markdown
## Image Optimization

### Issues Found
1. 🔴 `<img>` used instead of `next/image` in `app/about/page.tsx`
   - Current: `<img src="/hero.jpg" />` (unoptimized, no responsive)
   - Fix: `<Image src="/hero.jpg" width={1920} height={1080} priority alt="Hero" />`

2. 🔴 No `priority` on above-fold images in `app/page.tsx`
   - LCP element (hero image) loads with normal priority
   - Fix: Add `priority` prop to hero `next/image`

3. 🟡 No `sizes` attribute on responsive images
   - Browser downloads full-size image for all viewports
   - Fix: `sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"`

4. 🟡 Using PNG for photos instead of WebP/AVIF
   - PNG hero image: 850KB
   - WebP equivalent: 180KB (79% smaller)
   - Fix: `next/image` auto-serves WebP/AVIF with proper Accept header
```

### Step 5: Data Fetching Audit

Check for N+1 queries and unnecessary serialization:

```markdown
## Data Fetching Issues

### N+1 Query in `app/blog/page.tsx`
- Current: fetches all posts, then fetches author for each post (12 queries)
- Fix: Use Prisma `include` or `select` to fetch with join
```ts
// Before (N+1)
const posts = await prisma.post.findMany();
const postsWithAuthors = await Promise.all(
  posts.map(post => prisma.user.findUnique({ where: { id: post.authorId } }))
);

// After (1 query)
const postsWithAuthors = await prisma.post.findMany({
  include: { author: { select: { name: true, avatar: true } } }
});
```

### Unnecessary Data in Server → Client Serialization
- Current: Sending entire user object (including passwordHash) to client component
- Fix: Select only needed fields
```

### Step 6: Generate Optimization Report

```markdown
# ⚡ Next.js Performance Report

## Before vs After (Projected)

| Metric | Current | Target | Method |
|--------|---------|--------|--------|
| LCP | 3.8s | 1.9s | Image priority + font optimization + SSG |
| CLS | 0.21 | 0.02 | Image dimensions + skeleton loaders |
| INP | 340ms | 150ms | Component memoization + startTransition |
| Lighthouse Score | 52 | 95+ | All above fixes combined |
| Initial JS Bundle | 380KB | 142KB | Dynamic imports + dependency swaps |
| TTFB | 850ms | 120ms | ISR + Edge runtime |

## Priority Fixes (Do in This Order)

### 🔴 Critical (Do Today)
1. Switch `<img>` to `next/image` with `priority` on LCP element
2. Move homepage from SSR to SSG + ISR
3. Replace moment.js with date-fns
4. Add `dynamic()` import for Charts component

### 🟡 Important (This Week)
5. Add `sizes` to all responsive images
6. Memoize expensive list items
7. Fix N+1 query in blog page
8. Switch /pricing to SSG

### 🔵 Nice to Have (This Sprint)
9. Switch /api/products to Edge runtime
10. Add loading.tsx for all route segments
11. Implement `next/font` for all custom fonts
```

## Output Constraints

- Every recommendation must include the current code and the fixed code
- Performance projections must be realistic (not "100x faster")
- Fixes must be ordered by impact × ease (critical first)
- Must distinguish between App Router and Pages Router recommendations
- All code examples must be TypeScript

## What This Skill Does NOT Do

- Does not run Lighthouse or PageSpeed Insights (provides the fixes to improve scores)
- Does not modify production code (generates recommendations and code snippets)
- Does not handle non-Next.js React apps (use React component skill)
- Does not optimize backend database performance (suggests query fixes only)
