---
name: orshot
description: Generate images, PDFs, and videos from templates with Orshot — via the REST API, SDKs (Node/Python/PHP/Ruby), the remote MCP server, or no-code tools (Zapier, Make, n8n, Airtable), and wire those renders into a recurring automation. Use whenever the user mentions Orshot, connects Orshot to an AI agent or MCP client, wants a render to run unattended on a schedule or trigger, or needs to programmatically produce marketing visuals, OG images, social carousels, certificates/invoices/tickets as PDF, or video from templates — including when migrating from Bannerbear, Placid, Creatomate, RenderForm, Abyssale, or similar. Always load this skill for Orshot tasks, even simple ones, because it carries gotchas (modifications key by parameterId, multi-page needs a page1@ prefix, video output needs video elements in the template) that otherwise cause failed renders. Not for generating standalone AI images with no template or Orshot involved.
metadata:
  author: Rishi Mohan
  version: "1.1.0"
---

# Orshot – Automated Visual Content Generation

[Orshot](https://orshot.com) is an automated image, PDF, and video generation platform. Design templates in Orshot Studio (or import from Canva/Figma), then generate renders via REST API, SDKs, or no-code integrations.

- **Documentation:** https://orshot.com/docs
- **API Base URL:** https://api.orshot.com/v1

## When to Use This Skill

Use this skill whenever the user mentions **Orshot**, or when the task is:

- Generating images, PDFs, or videos programmatically from templates
- Building automated marketing visual pipelines (OG images, ad creatives, thumbnails)
- Creating dynamic social media content (carousels, posts, stories) and publishing it
- Generating certificates, invoices, tickets, or reports as PDFs
- Building image/PDF/video generation into a product
- Automating visuals with Zapier, Make, n8n, Airtable, or the CLI
- Connecting Orshot to an AI agent or MCP client (Claude, Cursor, Codex, Windsurf, ChatGPT)
- Embedding a white-label design editor into an app
- Migrating from Bannerbear, Placid, Creatomate, RenderForm, Abyssale, DynaPictures, or Contentdrips

**Don't use this skill** for generating standalone AI images with no template or Orshot involved (a one-off "make me an image" request) — that isn't what Orshot does.

## Accessing Detailed Documentation

Any page on orshot.com can be fetched as clean markdown by appending `.md` to the URL or sending `Accept: text/markdown` header. Use this to get detailed, up-to-date information on demand without relying solely on this skill file.

**Examples:**
```
https://orshot.com/docs/api-reference.md
https://orshot.com/docs/sdks/node.md
https://orshot.com/docs/publish/publish-from-api.md
https://orshot.com/docs/developers/oauth-overview.md
https://orshot.com/docs/orshot-embed/introduction.md
https://orshot.com/blog/bannerbear-api-alternative.md
```

**Key documentation pages:**
| Topic | URL |
|-------|-----|
| API Reference | `https://orshot.com/docs/api-reference.md` |
| Node.js SDK | `https://orshot.com/docs/sdks/node.md` |
| Python SDK | `https://orshot.com/docs/sdks/python.md` |
| PHP SDK | `https://orshot.com/docs/sdks/php.md` |
| Ruby SDK | `https://orshot.com/docs/sdks/ruby.md` |
| Studio Templates | `https://orshot.com/docs/orshot-studio/introduction.md` |
| Style Parameters | `https://orshot.com/docs/orshot-studio/style-parameters.md` |
| Setting Parameters | `https://orshot.com/docs/orshot-studio/setting-parameters.md` |
| Image Generation | `https://orshot.com/docs/image-generation.md` |
| Video Generation | `https://orshot.com/docs/video-generation.md` |
| PDF Generation | `https://orshot.com/docs/pdf-generation.md` |
| Social Publishing | `https://orshot.com/docs/publish/introduction.md` |
| OAuth / Developer Apps | `https://orshot.com/docs/developers.md` |
| White-Label Embed | `https://orshot.com/docs/orshot-embed/introduction.md` |
| Integrations | `https://orshot.com/docs/integrations.md` |
| Dynamic URLs | `https://orshot.com/docs/integrations/dynamic-urls.md` |
| Webhooks | `https://orshot.com/docs/integrations/webhooks.md` |
| Error Reference | `https://orshot.com/docs/error-reference.md` |

When a user asks about a specific topic, fetch the relevant `.md` URL for the latest details.

## Getting Started

### Authentication

All API requests require a Bearer token in the `Authorization` header:

```
Authorization: Bearer <ORSHOT_API_KEY>
```

[Get your API key](https://orshot.com/docs/quick-start/get-api-key) from **Workspace Settings → API Keys** in the Orshot dashboard.

### Remote MCP Server

Orshot runs a hosted MCP server so agents (Claude, Cursor, Codex, Windsurf, ChatGPT, etc.) can use Orshot as tools — no local install.

- **URL:** `https://mcp.orshot.com/mcp` (transport: `streamable-http`)
- **Auth:** OAuth 2.0 (the client walks you through it), or send an Orshot API key as a Bearer token
- **Claude Code:** `claude mcp add --transport http orshot https://mcp.orshot.com/mcp`
- **Cursor / Windsurf / VS Code / ChatGPT / Codex:** add the URL as a remote/HTTP MCP server

It exposes tools for rendering, studio + library templates, brand assets, workflows, social accounts, and workspace/logs. Full discovery doc: `https://orshot.com/.well-known/mcp.json`. Setup guide: `https://orshot.com/docs/integrations/mcp-server.md`.

### SDKs

#### Node.js

```bash
npm install orshot
```

```js
import { Orshot } from "orshot";
const orshot = new Orshot("<ORSHOT_API_KEY>");

// Render from template
const response = await orshot.renderFromTemplate({
  templateId: "open-graph-image-1",
  modifications: { title: "Hello World" },
  responseType: "base64", // "base64" | "url" | "binary"
  responseFormat: "png", // "png" | "webp" | "jpg" | "pdf"
});

// Generate signed URL
const signedUrl = await orshot.generateSignedUrl({
  templateId: "open-graph-image-1",
  modifications: { title: "Hello" },
  expiresAt: 1744276943,
  renderType: "images",
  responseFormat: "png",
});
```

#### Python

```bash
pip install orshot
```

```python
import orshot
os = orshot.Orshot('<ORSHOT_API_KEY>')

response = os.render_from_template({
  'template_id': 'open-graph-image-1',
  'modifications': {'title': 'Hello World'},
  'response_type': 'base64',
  'response_format': 'png'
})
```

#### Other SDKs

- **PHP:** `composer require rishimohan/orshot`
- **Ruby:** `gem install orshot`

## Common Gotchas (read before rendering)

The mistakes that most often make Orshot calls fail or return the wrong output:

1. **Modifications key by `parameterId`, not layer name.** `modifications: { "headline": "..." }` targets the element whose `parameterId` is `headline`. If a value is ignored, the key is wrong — fetch the template's modifications (`GET /v1/studio/templates/:id`) to see the real keys instead of guessing.
2. **Multi-page templates need a `pageN@` prefix.** Use `"page1@title"`, `"page2@title"`. A bare `"title"` only affects page 1.
3. **Studio `templateId` is an integer; utility `templateId` is a string.** `/v1/studio/render` takes an integer ID; `/v1/generate/:renderType` takes a string slug like `"website-screenshot"`.
4. **Video output requires video elements in the template.** Requesting `format: "mp4"` on an image-only template fails — the template must contain at least one video element.
5. **Image/video URLs in modifications must be publicly reachable.** The renderer fetches them server-side, so `localhost`, expired signed URLs, or auth-gated URLs won't load.
6. **Style overrides use dot notation on the parameterId** — `"title.fontSize": "48px"`, not a nested object.
7. **Response shape differs by page count:** single page → `data` is an object (read `data.content`); multi-page/carousel → `data` is an array of `{ page, content }`. Handle both.
8. **`base64` and `binary` response types don't combine** — `binary` returns one raw file stream.
9. **Credits vs AI Credits are separate** — normal renders spend credits; `.prompt` (AI) modifications additionally spend AI Credits.
10. **On `429`, back off** using the `Retry-After` response header.

When unsure about a template's parameters, always fetch its modifications first.

## Template Architecture

This section describes the complete structure of an Orshot template for MCP tools and AI agents.

### Template Structure

An Orshot template consists of **pages**, each containing a **canvas** and **elements**.

```
Template
├── id: number | string
├── name: string
├── description: string
├── width: number
├── height: number
├── pages_data: Array
    └── Page
        ├── id: string (UUID)
        ├── name: string
        ├── canvas: CanvasConfig
            ├── width: number
            ├── height: number
            ├── backgroundColor: string
            ├── backgroundImage: string
        ├── elements: Element[]
        ├── modifications: Modification[] (API parameters)
            ├── id: string
            ├── type: string
            ├── element: Element
            ├── description: string
        └── thumbnail_url: string | null
```

### Canvas Configuration

| Property          | Type   | Default         | Description                               |
| ----------------- | ------ | --------------- | ----------------------------------------- |
| `width`           | number | 800             | Canvas width in pixels (max: 5000)        |
| `height`          | number | 800             | Canvas height in pixels (max: 5000)       |
| `backgroundColor` | string | "#ffffff"       | Background color (hex, rgba, or gradient) |
| `backgroundImage` | string | ""              | URL to background image                   |
| `borderWidth`     | number | 0               | Border width in pixels                    |
| `borderColor`     | string | "rgba(0,0,0,1)" | Border color                              |
| `borderStyle`     | string | "solid"         | Border style (solid, dashed, etc)         |

### Canvas Size Presets

| Name                 | Dimensions | Use Case                        |
| -------------------- | ---------- | ------------------------------- |
| Square               | 1080×1080  | Instagram posts, general social |
| Instagram Story      | 1080×1920  | Stories, Reels, TikTok          |
| Slide/Presentation   | 1920×1080  | Presentations, slides           |
| YouTube Thumbnail    | 1280×720   | Video thumbnails                |
| Twitter Post         | 1600×900   | X/Twitter posts                 |
| Open Graph           | 1200×630   | Link previews, Facebook         |
| Pinterest Pin        | 1000×1500  | Pinterest                       |
| A4 Document          | 2480×3508  | Print documents                 |
| App Store Screenshot | 1290×2796  | iOS app screenshots             |

### Universal Element Properties

All elements share these base properties:

| Property            | Type    | Description                                  |
| ------------------- | ------- | -------------------------------------------- |
| `id`                | string  | Unique identifier (UUID)                     |
| `name`              | string  | Display name in layer list (was `layerName`) |
| `type`              | string  | "text", "image", "shape", "video"            |
| `position`          | object  | `{ x: number, y: number }` from top-left     |
| `dimensions`        | object  | `{ width: number, height: number }`          |
| `rotation`          | number  | Rotation in degrees (0-360)                  |
| `zIndex`            | number  | Layer order (higher = on top)                |
| `aspectRatioLocked` | boolean | Lock aspect ratio during resize              |
| `isHidden`          | boolean | Hide element from render                     |
| `skewX`             | number  | Horizontal skew angle                        |
| `skewY`             | number  | Vertical skew angle                          |

### Text Element

**Content Types:**

- **Plain text**: `"Hello World"` - Standard text string
- **Multi-line**: Use `\n` for line breaks: `"Line 1\nLine 2"`
- **Dynamic via API**: Use `.prompt` modifier for AI-generated text

```javascript
{
  type: "text",
  content: string,          // Plain text string
  layerName: string,        // Display name
  zIndex: number,
  rotation: number,
  position: { x: number, y: number },
  dimensions: { width: number, height: number },
  style: {
    // Typography
    fontFamily: string,     // e.g., "Inter", "Prata", "SF Pro"
    fontSize: string,       // e.g., "48px"
    fontWeight: string | number, // "400", "700", 700
    fontStyle: string,      // "normal", "italic"
    lineHeight: number,     // e.g., 1.2
    letterSpacing: string,  // e.g., "0px", "2px"

    // Appearance
    fill: string,           // Color or gradient
    color: string,          // Hex or rgba
    opacity: number,        // 0-1
    stroke: string,         // Stroke color
    strokeWidth: string,    // e.g., "0px"

    // Alignment & Layout
    textAlign: string,      // "left", "center", "right"
    verticalAlign: string,  // "flex-start", "center", "flex-end"
    textTransform: string,  // "none", "uppercase"
    textDecoration: string, // "none", "underline"
    textMode: string,       // "overflow", "fit"
    paddingX: string,
    paddingY: string,

    // Borders & Backgrounds
    borderColor: string,
    borderWidth: string,
    borderRadius: string,
    textBackgroundColor: string,
    textBackgroundRadius: string,
    textStrokeColor: string,
    textStrokeWidth: string,

    // Effects
    minFontSize: string,    // For "fit" mode
    filter: string,         // e.g., "blur(0px)"
    mixBlendMode: string,   // "normal", "multiply", etc.
    boxShadowX: string,
    boxShadowY: string,
    boxShadowBlur: string,
    boxShadowColor: string,
    dropShadowX: string,
    dropShadowY: string,
    dropShadowBlur: string,
    dropShadowColor: string
  },
  // Parameterization
  parameterizable: boolean,
  parameterId: string,
  parameterType: "text"
}
```

**Gradient text:**

```javascript
color: "linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%)";
```

### Image Element

**Content Types:**

- **URL** (recommended): `"https://example.com/image.png"` - Best for dynamic content
- **Base64**: `"data:image/png;base64,iVBORw0KGgo..."` - For embedded images
- **Binary**: Raw binary data (API upload only)

```javascript
{
  type: "image",
  content: string,          // URL (preferred), base64, or binary
  isSvg: boolean,
  layerName: string,
  style: {
    // Sizing & Positioning
    objectFit: string,      // "contain", "cover", "fill"
    objectPosition: string, // "center", "top left"

    // Appearance
    opacity: number,
    fill: string,           // Background fill
    stroke: string,         // Border stroke

    // Borders
    borderRadius: string,   // "0px", "12px", "50%"
    borderWidth: string,
    borderColor: string,

    // Effects
    filter: string,         // "blur(2px)", "grayscale(100%)"
    mixBlendMode: string,
    boxShadowX: string,
    boxShadowY: string,
    boxShadowBlur: string,
    boxShadowColor: string,
    dropShadowX: string,
    dropShadowY: string,
    dropShadowBlur: string,
    dropShadowColor: string,

    svgColor: string        // Recolor monochrome SVGs
  },
  parameterType: "imageUrl"
}
```

### Shape Element

```javascript
{
  type: "shape",
  shapeType: string,        // "rectangle", "circle", "arrow"
  layerName: string,
  style: {
    // Fill & Stroke
    fill: string,           // Color or gradient
    stroke: string,
    strokeWidth: string,    // e.g. "0px"

    // Dimensions
    borderRadius: string,   // Rectangle only
    borderWidth: string,
    borderColor: string,
    borderStyle: string,

    // Appearance
    opacity: number,
    filter: string,
    mixBlendMode: string,

    // Shadows
    boxShadowX: string,
    boxShadowY: string,
    boxShadowBlur: string,
    boxShadowColor: string,
    dropShadowX: string,
    dropShadowY: string,
    dropShadowBlur: string,
    dropShadowColor: string
  },
  parameterType: "fill"
}
```

**Gradient fills:**

```javascript
fill: "linear-gradient(180deg, rgba(0,0,0,0.7) 0%, transparent 100%)";
fill: "radial-gradient(circle at center, #FF6B6B 0%, #4ECDC4 100%)";
```

### Video Element

**Content Types:**

- **URL** (required): `"https://example.com/video.mp4"` - Must be a publicly accessible URL
- Supported formats: MP4, WebM, MOV
- For best results, use MP4 with H.264 codec

```javascript
{
  type: "video",
  content: string,          // Video URL (must be publicly accessible)
  videoOptions: {
    loop: boolean,
    muted: boolean,
    trim_start_time: string,
    trim_end_time: string,
    duration: number | null
  },
  style: {
    // Sizing & Positioning
    objectFit: string,      // "contain", "cover", "fill"
    objectPosition: string,

    // Appearance
    opacity: number,
    filter: string,
    mixBlendMode: string,

    // Borders & Shadows
    borderRadius: string,
    borderWidth: string,
    borderColor: string,
    elementBoxShadowX: string,
    elementBoxShadowY: string,
    elementBoxShadowBlur: string,
    elementBoxShadowColor: string
  },
  parameterType: "videoUrl"
}
```

### Parameterization Best Practices

When creating or updating templates, **always ensure all text, image, and video elements are parameterizable** with unique IDs. This enables dynamic content replacement via the API.

#### Required Setup

Every dynamic element MUST have:

```javascript
{
  parameterizable: true,
  parameterId: "unique_id",  // Unique across template, lowercase with underscores
  parameterType: "text" | "imageUrl" | "videoUrl"
}
```

#### Naming Conventions

| Element Type | parameterId Examples                        | parameterType |
| ------------ | ------------------------------------------- | ------------- |
| Text         | `headline`, `subtitle`, `cta_text`, `price` | `"text"`      |
| Image        | `product_image`, `logo`, `background_image` | `"imageUrl"`  |
| Video        | `hero_video`, `background_video`            | `"videoUrl"`  |

#### Best Practices

1. **Use descriptive IDs:** `product_title` not `text1`
2. **Be consistent:** Use snake_case across all templates
3. **Unique per template:** No duplicate parameterIds on same page
4. **Group logically:** Related elements share naming prefix (e.g., `card_title`, `card_image`)

#### Validation Checklist

Before finalizing any template update:
- [ ] All text elements have `parameterizable: true` and unique `parameterId`
- [ ] All image elements have `parameterizable: true` and unique `parameterId`
- [ ] All video elements have `parameterizable: true` and unique `parameterId`
- [ ] No duplicate parameterIds exist on the same page
- [ ] parameterIds are descriptive and follow snake_case convention

### Design Best Practices

#### Typography Guidelines
- **Font limit:** Use 2-3 fonts maximum per template
- **Hierarchy:** Headings should be 1.5-2x larger than body text
- **Minimum size:** 24px for social media readability
- **Weights:** Headings 600-900 (bold), Body 400-500 (regular)

**Popular font pairings:**
- `Prata` + `Inter`
- `Instrument Serif` + `DM Sans`
- `Playfair Display` + `Lato`
- `Montserrat` + `Open Sans`

**Platform-specific fonts:**
- iOS: `SF Pro Display`, `SF Pro Text`
- Android: `Google Sans`, `Roboto`

#### Color Guidelines
**Luxury/Gold palette:**
- Gold: `#D4AF37`
- Dark gold: `#B8860B`
- Light gold: `#F5E7A3`

**iOS system colors:**
- Blue: `#007AFF`
- Gray: `#8E8E93`
- Background: `#F5F5F7`

**Professional dark:**
- Navy: `#0F172A`
- Slate: `#1E293B`, `#334155`
- Muted: `#64748B`, `#94A3B8`

**Best practices:**
- Ensure 4.5:1 minimum contrast for text readability
- Use gradients sparingly for premium effects
- Consistent color palette (3-5 colors max)

#### Layout Guidelines
- **Edge padding:** 40-60px from canvas edges
- **Element spacing:** 20-40px between elements
- **Alignment:** Center for formal, left for modern
- **Visual flow:** Guide eye with size, color, position

**zIndex ordering:**
- Background images/colors: 1
- Overlay shapes: 2-3
- Text elements: 4-6
- Interactive elements: 7+

#### Common Operations (Design Automation)

**Add text element:**
```javascript
addElement("text", {
  content: "Hello World",
  fontFamily: "Inter",
  fontSize: 48,
  fontWeight: "700",
  color: "#FFFFFF",
  x: 100,
  y: 100,
  width: 400,
  height: 60,
});
```

**Add shape backdrop:**
```javascript
addElement("rectangle", {
  fill: "rgba(0,0,0,0.5)",
  width: 1080,
  height: 200,
  x: 0,
  y: 800,
  borderRadius: "0px",
});
```

**Batch update multiple elements:**
```javascript
batchUpdate([
  {
    elementId: "heading",
    type: "ORSHOT_UPDATE_ELEMENT",
    updates: { style: { fontSize: 72 } },
  },
  {
    elementId: "subtitle",
    type: "ORSHOT_UPDATE_ELEMENT",
    updates: { style: { color: "#94A3B8" } },
  },
  { type: "ORSHOT_UPDATE_CANVAS", updates: { backgroundColor: "#0F172A" } },
]);
```

## API Reference

### 1. Render from Studio Template

Generate images/PDFs/videos from templates designed in Orshot Studio.

**POST** `https://api.orshot.com/v1/studio/render`

```js
await fetch("https://api.orshot.com/v1/studio/render", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer <ORSHOT_API_KEY>",
  },
  body: JSON.stringify({
    templateId: 123, // Integer - your studio template ID
    modifications: {
      title: "Hello World",
      imageUrl: "https://example.com/photo.jpg",
      canvasBackgroundColor: "#eff2fa",
    },
    response: {
      type: "base64", // "base64" | "url" | "binary"
      format: "png", // "png" | "webp" | "jpg" | "pdf" | "mp4" | "webm" | "gif"
      scale: 1, // 1 = original size, 2 = double
      includePages: [1, 3], // optional – only for multi-page templates
      fileName: "my-render", // optional – custom filename (without extension)
    },
    pdfOptions: {
      // optional – only when format is "pdf"
      margin: "20px",
      rangeFrom: 1,
      rangeTo: 2,
      colorMode: "rgb", // "rgb" or "cmyk"
      dpi: 300,
    },
  }),
});
```

**Response (single page):**
```json
{
  "data": {
    "content": "data:image/png;base64,iVBORw0.....",
    "format": "png",
    "type": "base64",
    "responseTime": 325.22
  }
}
```

**Response (multi-page/carousel):**
```json
{
  "data": [
    { "page": 1, "content": "https://storage.orshot.com/.../image1.png" },
    { "page": 2, "content": "https://storage.orshot.com/.../image2.png" }
  ],
  "format": "png",
  "type": "url",
  "responseTime": 3166.01,
  "totalPages": 2,
  "renderedPages": 2
}
```

### 2. Render from Utility Template

Generate renders from Orshot's pre-built utility templates (e.g., website screenshots, tweet images).

**POST** `https://api.orshot.com/v1/generate/{renderType}`

- `renderType`: `images` or `pdfs`

```js
await fetch("https://api.orshot.com/v1/generate/images", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer <ORSHOT_API_KEY>",
  },
  body: JSON.stringify({
    templateId: "website-screenshot", // String ID for utility templates
    response: {
      format: "png",
      type: "base64",
    },
    modifications: {
      websiteUrl: "https://example.com",
      fullCapture: false,
      delay: 500,
      width: 1200,
      height: 1000,
    },
  }),
});
```

### 3. Generate Signed URL

Create publicly accessible render URLs without exposing your API key.

**POST** `https://api.orshot.com/v1/signed-url/create`

```js
await fetch("https://api.orshot.com/v1/signed-url/create", {
  method: "POST",
  headers: {
    Authorization: "Bearer <ORSHOT_API_KEY>",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    templateId: "website-screenshot",
    expiresAt: 1744550160505, // UNIX timestamp, or null for no expiry
    renderType: "images",
    modifications: {
      websiteUrl: "https://example.com",
    },
  }),
});
```

### 4. List Studio Templates

**GET** `https://api.orshot.com/v1/studio/templates/all?page=1&limit=10`

Response includes `data` array of templates and `pagination` object with `page`, `limit`, `total`, `totalPages`.

### 5. Get Studio Template

**GET** `https://api.orshot.com/v1/studio/templates/:templateId`

Returns the template metadata including available `modifications`.

### 6. Delete Studio Template

**DELETE** `https://api.orshot.com/v1/studio/templates/:templateId`

### 7. Duplicate Studio Template

**POST** `https://api.orshot.com/v1/studio/templates/:templateId/duplicate`

### 8. Get Profile & Workspaces

**GET** `https://api.orshot.com/v1/me`

Returns your profile and the workspaces your API key or OAuth token can access, including plan info and credit usage.

### 9. Brand Assets API

Brand assets are grouped by type — **images**, **colors**, **fonts**, **videos**, **audio** — each with its own routes under `/v1/brand-assets/{type}/…`.

#### Images
- **Get:** `GET https://api.orshot.com/v1/brand-assets/images/get`
- **Upload:** `POST https://api.orshot.com/v1/brand-assets/images/add` — `multipart/form-data` with a `file` field
- **Update tags:** `PATCH https://api.orshot.com/v1/brand-assets/images/update/:id`
- **Delete:** `DELETE https://api.orshot.com/v1/brand-assets/images/delete/:id`

#### Colors
- **Get:** `GET https://api.orshot.com/v1/brand-assets/colors/get`
- **Add:** `POST https://api.orshot.com/v1/brand-assets/colors/add` — body `{ type: "hex" | "gradient", value, tags? }`
- **Update tags:** `PATCH https://api.orshot.com/v1/brand-assets/colors/update/:id`
- **Delete:** `DELETE https://api.orshot.com/v1/brand-assets/colors/delete/:id`

#### Fonts / Videos / Audio
Same shape — swap the type segment (`fonts`, `videos`, `audio`):
- **Get:** `GET /v1/brand-assets/{type}/get`
- **Upload:** `POST /v1/brand-assets/{type}/add` (`multipart/form-data`, `file` field)
- **Update tags:** `PATCH /v1/brand-assets/{type}/update/:id`
- **Delete:** `DELETE /v1/brand-assets/{type}/delete/:id`

#### Search
- **Search assets:** `GET https://api.orshot.com/v1/brand-assets/search`

Use an uploaded asset in a render by passing its hosted URL as an image/video modification value.

### 10. Enterprise API Endpoints

These endpoints require an Enterprise plan.

#### Create Studio Template
**POST** `https://api.orshot.com/v1/studio/templates/create`

```js
{
  name: "Product Banner",        // required, max 255 chars
  description: "Banner template", // optional
  canvas_width: 1200,             // required, 1-5000
  canvas_height: 628,             // required, 1-5000
  pages_data: [...]               // optional - array of page objects with elements
}
```

#### Bulk Create Studio Templates
**POST** `https://api.orshot.com/v1/studio/templates/bulk-create`
Create multiple templates at once via CSV or JSON.

#### Update Template
**PATCH** `https://api.orshot.com/v1/studio/templates/:templateId`
Update template name and description.

#### Update Template Modifications
**PATCH** `https://api.orshot.com/v1/studio/templates/:templateId/update-modifications`
Update text and image content in template layers.

#### Generate Template Variants
**POST** `https://api.orshot.com/v1/studio/templates/:templateId/generate-variants`
Generate multiple size variants of a template using AI.

### 11. Dynamic URLs

Generate images directly from URL parameters:

```
https://api.orshot.com/v1/studio/dynamic-url/my-image?title=Hello%20World&title.fontSize=48px&title.color=%23ff0000
```
URL-encode special characters (e.g., `#` → `%23`).

### 12. Template Folders & Sharing

Organize studio templates into folders and share them:

- **List folders:** `GET https://api.orshot.com/v1/studio/folders`
- **Create folder:** `POST https://api.orshot.com/v1/studio/folders`
- **Update folder:** `PATCH https://api.orshot.com/v1/studio/folders/:folderId`
- **Delete folder:** `DELETE https://api.orshot.com/v1/studio/folders/:folderId`
- **Move template into folder:** `PATCH https://api.orshot.com/v1/studio/templates/:templateId/folder`
- **Get template sharing:** `GET https://api.orshot.com/v1/studio/templates/:templateId/share`
- **Update template sharing:** `POST https://api.orshot.com/v1/studio/templates/:templateId/share`

### 13. Workflows API

Workflows automate multi-step pipelines (trigger → fetch data → render → publish/deliver). Available to first-party clients (like the Orshot MCP server) and Enterprise workspaces.

- **List workflows:** `GET https://api.orshot.com/v1/workflows`
- **Create workflow:** `POST https://api.orshot.com/v1/workflows`
- **Get workflow:** `GET https://api.orshot.com/v1/workflows/:id`
- **Update workflow:** `PATCH https://api.orshot.com/v1/workflows/:id`
- **Delete workflow:** `DELETE https://api.orshot.com/v1/workflows/:id`
- **Run workflow:** `POST https://api.orshot.com/v1/workflows/:id/run`
- **List runs:** `GET https://api.orshot.com/v1/workflows/:id/runs`
- **Get a run:** `GET https://api.orshot.com/v1/workflows/:id/runs/:runId`
- **Validate a workflow:** `POST https://api.orshot.com/v1/workflows/validate`
- **List available nodes:** `GET https://api.orshot.com/v1/workflows/nodes`
- **Get/update sharing:** `GET` / `POST https://api.orshot.com/v1/workflows/:id/share`

## Render Configuration

### Dynamic Parameters

Override template styles, content, and behavior at render time using dot notation.

#### Style Parameters

Format: `parameterId.property`

```json
{
  "modifications": {
    "title": "Hello World",
    "title.fontSize": "48px",
    "title.color": "#ff0000",
    "title.fontFamily": "Roboto",
    "title.textAlign": "center",
    "logo.borderRadius": "50%",
    "logo.objectFit": "cover"
  }
}
```

**Text properties:** `fontSize`, `fontWeight`, `fontStyle`, `fontFamily`, `lineHeight`, `letterSpacing`, `textAlign`, `verticalAlign`, `textDecoration`, `textTransform`, `color`, `backgroundColor`, `backgroundRadius`, `textStrokeWidth`, `textStrokeColor`, `opacity`, `filter`, `dropShadowX/Y/Blur/Color`

**Image properties:** `objectFit`, `objectPosition`, `borderRadius`, `borderWidth`, `borderColor`, `boxShadowX/Y/Blur/Color`, `opacity`, `filter`

**Shape properties:** `fill`, `stroke`, `strokeWidth`, `borderRadius`, `opacity`

**Position/Size (all elements):** `x`, `y`, `width`, `height`

Property names are **case-insensitive**.

#### Multi-Page Templates

Prefix modifications with page number:
```json
{
  "modifications": {
    "page1@title": "Page 1 Title",
    "page2@title": "Page 2 Title",
    "page1@title.fontSize": "48px"
  }
}
```

#### AI Content Generation (.prompt)

Generate text or images using AI:
```json
{
  "modifications": {
    "headline.prompt": "Write a catchy headline about coffee",
    "background.prompt": "A serene mountain landscape at sunset"
  }
}
```
- `.prompt` on a text element generates copy; on an image element it generates imagery. The underlying AI models are managed by Orshot and may change over time — don't hardcode a specific model. AI modifications consume AI Credits.

#### Interactive Links (.href)

Add clickable links in PDF outputs:
```json
{
  "modifications": {
    "cta_button.href": "https://example.com/signup",
    "logo.href": "https://company.com"
  },
  "response": { "format": "pdf" }
}
```

#### Video Parameters

Control video elements dynamically:
```json
{
  "modifications": {
    "bgVideo": "https://example.com/video.mp4",
    "bgVideo.trimStart": 5,
    "bgVideo.trimEnd": 15,
    "bgVideo.muted": false,
    "bgVideo.loop": true
  },
  "response": { "format": "mp4" }
}
```

### Video Render Example

Render templates with video elements as MP4, WebM, or GIF:

```js
await fetch("https://api.orshot.com/v1/studio/render", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer <ORSHOT_API_KEY>",
  },
  body: JSON.stringify({
    templateId: 123,
    modifications: {
      videoElement: "https://example.com/custom-video.mp4",
      "videoElement.trimStart": 0,
      "videoElement.trimEnd": 10,
      "videoElement.muted": false,
      "videoElement.loop": true,
    },
    videoOptions: {
      trimStart: 0,
      trimEnd: 20,
      muted: true,
      loop: true,
    },
    response: {
      type: "url",
      format: "mp4",
    },
  }),
});
```

### Smart Resize (one design → any size)

Render a template at a **different canvas size without redesigning it** — the layout is deterministically re-solved to fit (elements re-anchor, backgrounds stretch, groups move together). Set these on the `response` object:

- **`size`** — *replace* the render size. A preset slug (`"instagram-story"`, `"og-image"`, `"youtube-thumbnail"`, …), a `"WIDTHxHEIGHT"` string (`"1080x1920"`), or use `width` + `height` (10–5000px each).
- **`extraSizes`** — *add* the same design at extra sizes in one call. An array (`["1080x1920", "1080x1080"]`) or a named object (`{ story: "1080x1920", square: "1080x1080" }`). Each output gains a nested `extraSizes` array of `{ size, width, height, content }`.

```json
{
  "templateId": 123,
  "modifications": { "title": "Launch Day" },
  "response": {
    "type": "url",
    "format": "png",
    "size": "1200x630",
    "extraSizes": ["1080x1920", "1080x1080"]
  }
}
```

Image formats only (`png`/`jpg`/`webp`/`avif`), up to 50 extra outputs per call. Each extra output is billed like a page (1 credit). Saved sizes from the Studio Smart Resize panel reproduce their approved preview exactly.

### Response Types

| Type     | Description                                     |
| -------- | ----------------------------------------------- |
| `url`    | Returns a hosted URL to the rendered file       |
| `base64` | Returns base64-encoded content as a string      |
| `binary` | Returns binary file content for custom handling |

### Response Formats

| Format | Type  | Notes                                      |
| ------ | ----- | ------------------------------------------ |
| `png`  | Image | Best quality, larger size                  |
| `webp` | Image | Smaller size, good quality                 |
| `jpg`  | Image | Compressed, no transparency                |
| `avif` | Image | Smallest size, modern browsers             |
| `pdf`  | Doc   | Supports multi-page, clickable links, CMYK |
| `mp4`  | Video | H.264, requires video elements in template |
| `webm` | Video | VP9, web-optimized                         |
| `mov`  | Video | QuickTime container                        |
| `mkv`  | Video | Matroska container                         |
| `gif`  | Video | Animated, no audio support                 |

### Render Usage & Costs

Usage is measured in **credits**. 1 credit = 1 image, 1 PDF page, or 1 second of video.

| Output               | Cost                     |
| -------------------- | ------------------------ |
| Image (PNG/JPG/WebP/AVIF) | 1 credit per image  |
| PDF                  | 1 credit per page        |
| Video (MP4/WebM/MOV/MKV/GIF) | 1 credit per second |

Multi-page templates and Smart Resize extra sizes: each output page/size counts as its own credit. AI modifications (`.prompt`) additionally consume AI Credits.

## Common Recipes

End-to-end patterns for the jobs people most often automate with Orshot.

### OG image on every deploy
Render a studio template to a stable hosted URL and drop it into your `<meta>` tags.
```js
const { data } = await fetch("https://api.orshot.com/v1/studio/render", {
  method: "POST",
  headers: { "Content-Type": "application/json", Authorization: "Bearer <KEY>" },
  body: JSON.stringify({
    templateId: 123,
    modifications: { title: post.title, author: post.author },
    response: { type: "url", format: "png", size: "og-image" },
  }),
}).then((r) => r.json());
// <meta property="og:image" content={data.content} />
```

### Bulk-generate from a CSV (certificates, badges, invoices)
Loop rows and render one PDF each. Describe image layers with `.alt` for accessible PDFs.
```js
for (const row of rows) {
  await fetch("https://api.orshot.com/v1/studio/render", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: "Bearer <KEY>" },
    body: JSON.stringify({
      templateId: 456,
      modifications: { name: row.name, course: row.course, date: row.date },
      response: { type: "url", format: "pdf" },
      pdfOptions: { title: `${row.name} — Certificate` },
    }),
  });
}
```

### Render and auto-post to social in one call
Add a `publish` object (see Social Publishing) — no second request.
```js
body: JSON.stringify({
  templateId: 123,
  modifications: { title: "Launch day!" },
  response: { type: "url", format: "png" },
  publish: { accounts: [1, 2], content: "We just shipped 🚀" },
});
```

### One design, every social size (Smart Resize)
```js
response: { type: "url", format: "png", extraSizes: ["1080x1920", "1080x1080", "1200x630"] }
// each output gains a nested extraSizes[] of { size, width, height, content }
```

### Automate a recurring pipeline (Workflows)
Create a workflow (trigger → fetch data → render → publish/deliver) with `POST /v1/workflows`, then trigger it with `POST /v1/workflows/:id/run`. Inspect results via `GET /v1/workflows/:id/runs`. Best driven through the MCP server or the Workflows API on Enterprise/first-party clients.

See **Setting Up Recurring Automation** below for the full playbook, including how
to wire it into an n8n/Make/Zapier setup the user already runs.

## Setting Up Recurring Automation

A one-off render is a demo. The value shows up when it runs unattended. Pick the
road that matches where the user ALREADY works, not the one easiest to describe.

### Choose the road first

Check what they already run before pitching anything. `GET /v1/workspace/logs?limit=100`
returns a `source` on every row, which answers it factually:

| `source` in their logs | They already run | Lead with |
| --- | --- | --- |
| `n8n-integration` | n8n | Add a node to the n8n workflow they have |
| `orshot-make` | Make | Add a module to their scenario |
| `zapier-integration` | Zapier | Add an action to their Zap |
| `orshot-pipedream` | Pipedream | Add a step |
| `orshot-*-sdk`, `api`, `cli` | Their own code | Write the call into their repo |
| only `playground` / `orshot-mcp-server` | Nothing yet | Offer Orshot Workflows |

Never pitch a second orchestrator to someone who already has one. A user with a
live n8n setup wants this template added to it, not a new tool to learn.

If you have browser control or repo access, offer to DO the setup rather than
describe it. Whichever road you take, **run it once and show the resulting image
URL** before calling it done.

### Road A — Orshot Workflows (no orchestrator yet)

Orshot runs the whole loop: trigger, render, deliver. Over MCP:

1. `orshot_suggest_workflows` with the `templateId` — returns automations that
   fit this template, with draft-ready steps
2. `orshot_list_workflow_nodes` — use the EXACT node keys it returns. Invented
   keys (e.g. `render_studio_template`, `slack_send`) fail as `unknown node`;
   the real keys are `render`, `slack`, and so on
3. `orshot_list_connected_integrations` — see what is already connected
4. `orshot_get_workflow_connection_data` — resolve "my content sheet" into a
   concrete id, and confirm the name back to the user
5. `orshot_validate_workflow` — read `errors`, `warnings` AND `gated`. A `gated`
   entry means a plan block, not a config problem: the draft still saves, only
   activation is blocked, so tell the user which plan unlocks it instead of
   editing steps
6. `orshot_create_workflow` with `status: "draft"`, then share the edit link from
   the result — it opens pre-configured in their dashboard
7. `orshot_run_workflow` — prove it works, then they activate

**Scaffolding shapes.** If they have no data source ready, use
`webhook` → `webhook_body` → `render` → `orshot_url`. It is the only
trigger→source pair needing no OAuth AND it validates clean with empty configs,
so it is runnable immediately and they can POST to it from cron, their app, n8n,
or Make. A bare `schedule` → `render` is NOT runnable — it fails with "no data
source"; a schedule needs a source step after it.

### Road B — their existing automation platform

Every platform needs the same three things: endpoint, auth header, modification
keys. Get the exact keys first — never guess them:

```
orshot_get_studio_template_modifications   (or GET /v1/studio/templates/:id/modifications)
```

Then the call to drop in:

```http
POST https://api.orshot.com/v1/studio/render
Authorization: Bearer <ORSHOT_API_KEY>
Content-Type: application/json

{
  "templateId": 1234,
  "modifications": { "headline": "{{ row.title }}", "hero_image": "{{ row.image_url }}" },
  "response": { "type": "url", "format": "png" }
}
```

The response contains the rendered URL — map it to whatever the next step needs.

- **n8n** — HTTP Request node, POST, header auth, body as above. A dedicated
  Orshot node also exists in the n8n library.
- **Make** — HTTP "Make a request" module, or the Orshot app modules.
- **Zapier** — Webhooks by Zapier → POST, or the Orshot Zapier app.
- **Pipedream** — HTTP step; Orshot components are published.
- **Own code / cron** — any HTTP client. Use `response.type: "url"` in production
  so you are not moving base64 around, and keep the API key in an environment
  variable, never inline.

Recurring triggers that work well: a new spreadsheet/Airtable/Notion row, a
schedule, an inbound webhook, or a CMS publish event.

### Verify before you call it done

1. Trigger one real run
2. `orshot_list_workspace_logs` (or `GET /v1/workspace/logs`) — the new render
   appears with the `source` of whatever fired it, proving which system made it
3. Show the user the image URL from that run

If the render 403s, read the body: an expired key, an inactive subscription, and
a plan limit all return 403 with different messages. A plan block is not an auth
problem — do not retry it as one.

## Integrations & Helps

### Integrations Service Support
Orshot connects with:
- **No-code:** Zapier, Make (Integromat), n8n, Pipedream, Airtable
- **Storage:** Amazon S3, Cloudflare R2, Google Drive, Dropbox
- **Notifications:** Slack, Webhooks
- **Design:** Figma Plugin, Canva Import, Polotno Import
- **CLI:** `npx orshot-cli` for terminal-based generation
- **MCP Server:** Use with Claude, Cursor, Windsurf via MCP protocol
- **Embed:** White-label design editor for your app (React SDK, Vue SDK, iframe)

### Common Error Codes

| Code | Error                          | Fix                                          |
| ---- | ------------------------------ | -------------------------------------------- |
| 400  | `templateId missing`           | Add `templateId` to request body             |
| 400  | `Invalid API Key`              | Generate new key from dashboard              |
| 403  | `Authorization header missing` | Add `Authorization: Bearer <KEY>` header     |
| 403  | `Subscription inactive`        | Check usage or upgrade plan                  |
| 403  | `Template not found`           | Verify template ID belongs to your workspace |
| 403  | `Video on free plan`           | Upgrade to paid plan for video generation    |

### General Best Practices

1. **Use `url` response type** for production – avoids large base64 payloads
2. **Use `webp` format** for smaller file sizes with good quality
3. **Test in Playground** before coding – each template has an interactive playground
4. **Use style parameters** instead of creating multiple template variants
5. **Use consistent units** – stick to `px` for sizes
6. **Multi-page prefix** – always use `page1@paramId` format for carousel templates
7. **Cache renders** – use `?cache=false` query param to bypass cache when needed
8. **Handle errors** – check for 403/400 status codes and parse error messages

## Social Publishing

Publish rendered images/videos directly to 13+ social platforms via API. Supports Twitter/X, Instagram, LinkedIn, Pinterest, Facebook, TikTok, YouTube, Threads, Bluesky, Reddit, Telegram, Snapchat, and Google Business.

For detailed setup: fetch `https://orshot.com/docs/publish/introduction.md`

### Connect Accounts

Connect social accounts in **Workspace Settings → Social Accounts** in the Orshot dashboard. Each connected account gets a numeric ID used in API calls.

### Publish from API

Add the `publish` object to any render request:

```js
await fetch("https://api.orshot.com/v1/studio/render", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer <ORSHOT_API_KEY>",
  },
  body: JSON.stringify({
    templateId: 123,
    modifications: { title: "New Post" },
    response: { type: "url", format: "png" },
    publish: {
      accounts: [1, 3],          // Social account IDs
      content: "Check this out!", // Caption text (max 5000 chars)
      isDraft: false,             // true = save as draft
      schedule: {                 // Optional: schedule for later
        scheduledFor: "2026-04-25T14:00:00Z"
      },
      timezone: "America/New_York",
      platformOptions: {          // Per-account overrides (keyed by account ID)
        "1": { firstComment: "https://example.com" },     // LinkedIn
        "3": { title: "Pin Title", link: "https://..." }   // Pinterest
      }
    }
  }),
});
```

**Response includes publish status:**
```json
{
  "data": { "content": "https://storage.orshot.com/..." },
  "publish": [
    { "platform": "twitter", "username": "acme", "status": "published", "url": "https://x.com/..." },
    { "platform": "linkedin", "username": "acme", "status": "scheduled" }
  ]
}
```

**Format compatibility:**
- PDF cannot be published to any platform
- Video (mp4/webm/gif) cannot be published to Google Business
- Image (png/jpg/webp) cannot be published to TikTok or YouTube (video-only)

## Developer Apps & OAuth

Build third-party integrations with Orshot using OAuth 2.0. Register apps, authenticate users, and access their workspaces programmatically.

For detailed setup: fetch `https://orshot.com/docs/developers/oauth-overview.md`

### Register an App

1. Go to **Workspace Settings → Developer Apps** in Orshot dashboard
2. Create a new app with name, redirect URI, and required scopes
3. Receive `client_id` and `client_secret`

### OAuth 2.0 Flows

**Authorization Code Flow** (web apps):
```
GET https://orshot.com/oauth/authorize?
  response_type=code&
  client_id=YOUR_CLIENT_ID&
  redirect_uri=https://yourapp.com/callback&
  scope=workspace:templates:read workspace:templates:write render:generate
```

**Device Flow** (CLI/headless):
```
POST https://orshot.com/oauth/device/code
  client_id=YOUR_CLIENT_ID&
  scope=workspace:templates:read render:generate
```

### Token Exchange

```
POST https://orshot.com/oauth/token
  grant_type=authorization_code&
  code=AUTH_CODE&
  client_id=YOUR_CLIENT_ID&
  client_secret=YOUR_CLIENT_SECRET&
  redirect_uri=https://yourapp.com/callback
```

### Available Scopes

| Scope | Description |
|-------|-------------|
| `workspace:read` | List and read workspace details |
| `workspace:templates:read` | List and read templates |
| `workspace:templates:write` | Update template modifications via API |
| `render:generate` | Generate images, PDFs, and videos |
| `mcp:access` | Access via Model Context Protocol |
| `offline_access` | Long-lived refresh tokens |

For endpoint details: fetch `https://orshot.com/docs/developers/oauth-endpoints.md`

## White-Label Embed (Orshot Embed)

Embed Orshot's template editor into your application as a white-label component. Users can design and customize templates directly in your app.

For detailed setup: fetch `https://orshot.com/docs/orshot-embed/introduction.md`

### Quick Setup (iframe)

```html
<iframe
  src="https://orshot.com/embeds/YOUR_EMBED_ID?userId=USER_123"
  width="100%"
  height="600"
  frameborder="0"
></iframe>
```

### React SDK

```bash
npm install @orshot/react
```

```jsx
import { OrshotEmbed } from "@orshot/react";

<OrshotEmbed
  embedId="YOUR_EMBED_ID"
  userId="user_123"
  token="JWT_TOKEN"
  onRender={(data) => console.log("Rendered:", data)}
  onSave={(data) => console.log("Saved:", data)}
/>
```

### Vue SDK

```bash
npm install @orshot/vue
```

```vue
<template>
  <OrshotEmbed
    embed-id="YOUR_EMBED_ID"
    user-id="user_123"
    @render="onRender"
    @save="onSave"
  />
</template>
```

### Key Features

- **Per-user templates**: Pass `userId` to give each user their own template copies
- **JWT authentication**: Secure embed access with domain whitelist validation
- **Webhooks**: Get notified on render completion, template save, etc.
- **Custom buttons**: Add your own action buttons to the editor toolbar
- **PostMessage API**: Control the embed programmatically from your app

For React SDK details: fetch `https://orshot.com/docs/orshot-embed/react-sdk.md`
For Vue SDK details: fetch `https://orshot.com/docs/orshot-embed/vue-sdk.md`
For webhook setup: fetch `https://orshot.com/docs/orshot-embed/webhooks.md`

## Migrating from Other Platforms

This section maps authentication, endpoints, and request formats for migrating from competing platforms. For detailed comparison articles, fetch the corresponding blog post URL.

### Migration Playbook (any platform)

The API-call swap is the easy part (mapped per-platform below). The real work is recreating the design, because you can't import another platform's template JSON:

1. **Recreate the template in Orshot Studio** (or via `POST /v1/studio/templates/create`). Rebuild the layout, then mark every dynamic layer parameterizable with a clear `parameterId`.
2. **Map old field names → Orshot `parameterId`s.** Other platforms key by layer name, `image_url`, `payload`, etc.; Orshot keys by `parameterId`. Keep a lookup from old names to new ones.
3. **Swap the API call** using the tables below — almost always `Authorization: Bearer` + `POST /v1/studio/render`.
4. **Handle sync vs async.** Most platforms are async (submit → poll/webhook); Orshot renders **synchronously**, so delete the polling/webhook code and read `data.content` from the response.
5. **Verify the response shape** — single page is an object, multi-page is an array (Common Gotchas #7) — before cutting traffic over.

### Migrating from BannerBear

Blog: `https://orshot.com/blog/bannerbear-api-alternative.md`

**Authentication:**
| BannerBear | Orshot |
|------------|--------|
| `Authorization: Bearer BB_API_KEY` | `Authorization: Bearer ORSHOT_API_KEY` |

**Endpoint Mapping:**
| Action | BannerBear | Orshot |
|--------|-----------|--------|
| Generate image | `POST /v2/images` (async, returns 202) | `POST /v1/studio/render` (sync) |
| Generate image (sync) | `POST sync.api.bannerbear.com/v2/images` (10s timeout) | `POST /v1/studio/render` (sync by default) |
| List templates | `GET /v2/templates` | `GET /v1/studio/templates/all?page=1&limit=10` |
| Get template | `GET /v2/templates/:uid` | `GET /v1/studio/templates/:id` |
| Generate video | `POST /v2/videos` | `POST /v1/studio/render` with `format: "mp4"` |
| Multi-template batch | `POST /v2/collections` | Loop `POST /v1/studio/render` per template |

**Request Format Translation:**

BannerBear uses a `modifications` **array** with named layers:
```json
// BannerBear
{
  "template": "TEMPLATE_UID",
  "modifications": [
    { "name": "title", "text": "Hello World" },
    { "name": "hero", "image_url": "https://example.com/img.jpg" },
    { "name": "bg", "color": "#FF0000" }
  ]
}

// Orshot equivalent
{
  "templateId": 123,
  "modifications": {
    "title": "Hello World",
    "hero": "https://example.com/img.jpg",
    "canvasBackgroundColor": "#FF0000"
  },
  "response": { "type": "url", "format": "png" }
}
```

**Key differences:**
- BannerBear modifications is an **array**, Orshot is a **flat object**
- BannerBear uses `image_url` for images, Orshot uses the parameter ID directly with a URL value
- BannerBear requires polling for async results, Orshot returns synchronously
- BannerBear `template` is a UID string, Orshot `templateId` is an integer for studio templates
- Orshot supports style overrides via dot notation (e.g., `"title.fontSize": "48px"`) — BannerBear does not

### Migrating from Placid

Blog: `https://orshot.com/blog/placid-api-alternative.md`

**Authentication:**
| Placid | Orshot |
|--------|--------|
| `Authorization: Bearer PLACID_TOKEN` | `Authorization: Bearer ORSHOT_API_KEY` |

**Endpoint Mapping:**
| Action | Placid | Orshot |
|--------|--------|--------|
| Generate image | `POST /api/rest/{template_uuid}` | `POST /v1/studio/render` |
| Get image status | `GET /api/rest/images/{id}` | Not needed (sync response) |
| List templates | `GET /api/rest/templates` | `GET /v1/studio/templates/all?page=1&limit=10` |
| Get template | `GET /api/rest/templates/{uuid}` | `GET /v1/studio/templates/:id` |
| Delete render | `DELETE /api/rest/images/{id}` | Not needed (renders don't expire) |

**Request Format Translation:**

Placid uses a `layers` **object** with type-specific properties:
```json
// Placid
{
  "layers": {
    "title": {
      "text": "Hello World",
      "text_color": "#FF0000",
      "font": "Arial"
    },
    "hero_image": {
      "image": "https://example.com/img.jpg"
    },
    "background": {
      "background_color": "#000000"
    }
  },
  "modifications": {
    "width": 1200,
    "height": 630,
    "image_format": "jpg"
  }
}

// Orshot equivalent
{
  "templateId": 123,
  "modifications": {
    "title": "Hello World",
    "title.color": "#FF0000",
    "title.fontFamily": "Arial",
    "hero_image": "https://example.com/img.jpg",
    "canvasBackgroundColor": "#000000"
  },
  "response": { "type": "url", "format": "jpg" }
}
```

**Key differences:**
- Placid separates `layers` (content) from `modifications` (output settings), Orshot combines both in `modifications`
- Placid uses `text_color`, Orshot uses dot notation `parameterId.color`
- Placid uses `image` key for image URLs, Orshot uses the parameter ID directly
- Placid requires polling or webhooks, Orshot returns synchronously
- Placid renders can expire, Orshot renders persist
- Placid credits vary by resolution, Orshot is a flat 1 credit per image regardless of size

### Migrating from Creatomate

Blog: `https://orshot.com/blog/creatomate-api-alternative.md`

**Authentication:**
| Creatomate | Orshot |
|------------|--------|
| `Authorization: Bearer CREATOMATE_KEY` | `Authorization: Bearer ORSHOT_API_KEY` |

**Endpoint Mapping:**
| Action | Creatomate | Orshot |
|--------|-----------|--------|
| Generate render | `POST /v1/renders` | `POST /v1/studio/render` |
| Get render status | `GET /v1/renders/:id` | Not needed (sync response) |
| List templates | `GET /v1/templates` | `GET /v1/studio/templates/all?page=1&limit=10` |
| Get template | `GET /v1/templates/:id` | `GET /v1/studio/templates/:id` |

**Request Format Translation:**

Creatomate uses a flat `modifications` object (closest to Orshot's format):
```json
// Creatomate
{
  "template_id": "TEMPLATE_UUID",
  "modifications": {
    "Title": "Hello World",
    "Image-1": "https://example.com/img.jpg"
  },
  "output_format": "jpg",
  "render_scale": 1,
  "max_width": 1080
}

// Orshot equivalent
{
  "templateId": 123,
  "modifications": {
    "title": "Hello World",
    "image_1": "https://example.com/img.jpg"
  },
  "response": { "type": "url", "format": "jpg", "scale": 1 }
}
```

**Key differences:**
- Creatomate `template_id` is a UUID string, Orshot `templateId` is an integer
- Creatomate element names are display names (e.g., "Title", "Image-1"), Orshot uses snake_case parameterIds
- Creatomate has `output_format` at root level, Orshot uses `response.format`
- Creatomate requires polling/webhooks, Orshot returns synchronously
- Creatomate renders can expire, Orshot renders persist
- Orshot supports style overrides via dot notation — Creatomate requires modifying the template source JSON
- Creatomate gates its preview SDK to a higher tier; Orshot's embed is available on all paid plans

### Migrating from RenderForm

Blog: `https://orshot.com/blog/renderform-api-alternative.md`

**Authentication:**
| RenderForm | Orshot |
|------------|--------|
| `X-API-KEY: RENDERFORM_KEY` | `Authorization: Bearer ORSHOT_API_KEY` |

**Endpoint Mapping:**
| Action | RenderForm | Orshot |
|--------|-----------|--------|
| Generate image | `POST /api/v2/render` | `POST /v1/studio/render` |
| List templates | `GET /api/v2/my-templates?page=1&size=50` | `GET /v1/studio/templates/all?page=1&limit=10` |
| Get template | `GET /api/v2/my-templates/:id` | `GET /v1/studio/templates/:id` |
| URL-based render | `GET /img/TEMPLATE.jpg?key=...&param=...` | `GET /v1/studio/dynamic-url/TEMPLATE?param=...` |

**Request Format Translation:**

RenderForm uses dot notation in a `data` object (similar to Orshot's style overrides):
```json
// RenderForm
{
  "template": "TEMPLATE_ID",
  "data": {
    "title.text": "Hello World",
    "hero.src": "https://example.com/img.jpg",
    "bg.color": "#FF0000"
  },
  "fileName": "output",
  "width": 1200,
  "height": 630
}

// Orshot equivalent
{
  "templateId": 123,
  "modifications": {
    "title": "Hello World",
    "hero": "https://example.com/img.jpg",
    "canvasBackgroundColor": "#FF0000"
  },
  "response": { "type": "url", "format": "png", "fileName": "output" }
}
```

**Key differences:**
- RenderForm uses `X-API-KEY` header, Orshot uses `Authorization: Bearer`
- RenderForm uses `data` with `componentId.property` dot notation for everything, Orshot uses `modifications` with parameter IDs for content and dot notation only for style overrides
- RenderForm `template` is a string ID, Orshot `templateId` is an integer
- RenderForm images can expire, Orshot renders persist
- Orshot's free tier has no watermarks

### Migrating from Abyssale

Blog: `https://orshot.com/blog/abyssale-api-alternative.md`

**Authentication:**
| Abyssale | Orshot |
|----------|--------|
| `x-api-key: ABYSSALE_KEY` | `Authorization: Bearer ORSHOT_API_KEY` |

**Endpoint Mapping:**
| Action | Abyssale | Orshot |
|--------|---------|--------|
| Generate image | `POST /async/banner-builder/{designId}/generate` (async) | `POST /v1/studio/render` (sync) |
| Poll status | `GET /generation-request/{requestId}` | Not needed (sync response) |
| List designs | `GET /designs` | `GET /v1/studio/templates/all?page=1&limit=10` |
| Get design | `GET /designs/{designId}` | `GET /v1/studio/templates/:id` |
| Multi-format render | `template_format_names` param | Loop `POST /v1/studio/render` per format, or use Variant Generation API |

**Request Format Translation:**

Abyssale uses an `elements` object with `payload` for text:
```json
// Abyssale
{
  "template_format_names": ["facebook-feed", "instagram-post"],
  "elements": {
    "title": { "payload": "Hello World" },
    "hero_image": { "image_url": "https://example.com/img.jpg" },
    "background": { "color": "#FF0000" }
  },
  "callback_url": "https://webhook.example.com"
}

// Orshot equivalent
{
  "templateId": 123,
  "modifications": {
    "title": "Hello World",
    "hero_image": "https://example.com/img.jpg",
    "canvasBackgroundColor": "#FF0000"
  },
  "response": { "type": "url", "format": "png" }
}
```

**Key differences:**
- Abyssale uses `payload` for text content, Orshot uses the parameter ID directly
- Abyssale uses `image_url` for images, Orshot uses the parameter ID with URL value
- Abyssale supports multi-format in single call via `template_format_names`, Orshot requires separate calls or Variant Generation API
- Abyssale is async-only (polling/webhook), Orshot returns synchronously
- Abyssale charges per-seat, Orshot has unlimited team members on all plans
- Abyssale results can expire, Orshot renders persist

### Migrating from DynaPictures

Blog: `https://orshot.com/blog/dynapictures-api-alternative.md`

**Authentication:**
| DynaPictures | Orshot |
|--------------|--------|
| `Authorization: Bearer DYNA_KEY` | `Authorization: Bearer ORSHOT_API_KEY` |

**Endpoint Mapping:**
| Action | DynaPictures | Orshot |
|--------|-------------|--------|
| Generate image | `POST /designs/{id}` | `POST /v1/studio/render` |
| List designs | `GET /designs` | `GET /v1/studio/templates/all?page=1&limit=10` |

**Key differences:**
- DynaPictures uses an outdated editor interface, Orshot has a modern Figma-like editor
- No multi-page support in DynaPictures
- No white-label editor option
- Limited integrations compared to Orshot's 15+

### Migrating from Contentdrips

Blog: `https://orshot.com/blog/contentdrips-api-alternative.md`

Contentdrips is a social media design tool with API as a secondary feature. Migration is straightforward since Orshot is API-first.

**Key differences:**
- Contentdrips API is bolted-on, Orshot is API-first
- Contentdrips has limited dynamic parameter capabilities
- No white-label editor, no MCP server, no CLI
- Per-seat pricing vs. Orshot's credit-based pricing

### Quick Migration Reference

| Feature | BannerBear | Placid | Creatomate | RenderForm | Abyssale | Orshot |
|---------|-----------|--------|------------|------------|----------|--------|
| **Auth header** | `Authorization: Bearer` | `Authorization: Bearer` | `Authorization: Bearer` | `X-API-KEY` | `x-api-key` | `Authorization: Bearer` |
| **Modifications format** | Array of objects | `layers` object | Flat object | `data` with dot notation | `elements` with `payload` | Flat object |
| **Template ID type** | UID string | UUID string | UUID string | String | UUID string | Integer (studio) |
| **Response model** | Async (poll) | Async (poll) | Async (poll) | Sync | Async (poll) | Sync |
| **Render persistence** | Permanent | Can expire | Can expire | Can expire | Can expire | Permanent |
| **Style overrides** | No | Limited | Via source JSON | Dot notation | No | Dot notation |
| **Multi-page** | No | No | No | No | No | Yes |
| **Video support** | Yes (extra cost) | Yes (extra cost) | Yes | No | Animated only | Yes (1 credit/sec) |
| **White-label editor** | No | No | Higher tier | No | No | All paid plans |
| **Social publishing** | No | No | No | No | No | 13+ platforms |

### Links

- Documentation: https://orshot.com/docs
- API Reference: https://orshot.com/docs/api-reference
- Integrations: https://orshot.com/integrations
- MCP Server: https://orshot.com/docs/integrations/mcp-server
- Templates: https://orshot.com/templates
- Pricing: https://orshot.com/pricing
- Developer Apps: https://orshot.com/docs/developers
- Social Publishing: https://orshot.com/docs/publish/introduction
- Orshot Embed: https://orshot.com/docs/orshot-embed/introduction
