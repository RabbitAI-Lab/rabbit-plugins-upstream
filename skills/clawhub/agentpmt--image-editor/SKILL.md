---
name: image-editor
description: "Image Editor: Edit images: blur, crop, resize, rotate, invert colors. Use when an agent needs image editor, generating branded social media graphics by compositing logos onto product images, automating thumbnail creation by resizing and cropping uploaded images to standard dimensions, adding watermarks or copyright text overlays to protect visual content, creating placeholder images with custom colors and dimensions for ui mockups, blur, image base64, image url through AgentPMT-hosted remote."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/image-editor
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/image-editor"}}
---
# Image Editor

## Freshness
Last updated: `2026-06-23`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Edit and transform images without any design software. Resize, crop, rotate, blur, invert colors, add borders, draw shapes, overlay text, composite layers, remove backgrounds, and apply shear transforms — all from a single tool. Chain multiple operations together in one request to build complete editing workflows like watermarking, thumbnail generation, or branded graphics. Supports PNG, JPEG, and WebP input and output. Upload an image, provide a URL, or reference a file already in cloud storage, and get your edited result back as a stored file with a shareable link or as inline data ready to use immediately.

## Product Instructions
### Image Editor - Instructions

#### Overview
The Image Editor tool provides programmatic image manipulation capabilities including resizing, cropping, rotating, drawing shapes, adding text, compositing layers, applying blur effects, adding borders, creating transparent regions, inverting colors, and more. Operations can be chained together using multi_step mode.

#### Image Input
Every action (except `create`) requires an image input via one of:
- **image_url** - Public URL to a PNG, JPG, or WebP image
- **image_base64** - Base64-encoded image data
- **file_id** - File ID from cloud storage (from a previous upload or edit)

#### Common Output Options
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| output_format | string | `"png"` | Output format: `png`, `jpeg`, or `webp` |
| filename | string | `"edited.<ext>"` | Filename for the stored output |
| store_file | boolean | `true` | Store the result in cloud storage (returns file_id and signed_url) |
| return_base64 | boolean | `false` | Also return the image as inline base64 (max 10 MB) |

---

#### Actions

##### info
Get image dimensions and mode without modifying it.

**Required:** An image input (image_url, image_base64, or file_id)
**Optional params:** None

**Example:**
```json
{
  "action": "info",
  "image_url": "https://example.com/photo.png"
}
```

---

##### create
Create a new blank image canvas.

**Required:** None (defaults apply)
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| width | integer | 512 | Canvas width in pixels |
| height | integer | 512 | Canvas height in pixels |
| color | string/array | `"#ffffff"` | Fill color (hex string, RGB array, or RGBA array) |

**Example:**
```json
{
  "action": "create",
  "params": { "width": 800, "height": 600, "color": "#ff0000" }
}
```

---

##### resize
Resize an image to specific dimensions or by a scale factor.

**Required:** An image input + either `width`/`height` or `scale` in params
**Optional params:**
| Param | Type | Description |
|-------|------|-------------|
| width | integer | Target width in pixels |
| height | integer | Target height in pixels |
| scale | float | Scale factor (e.g., 0.5 for half size, 2.0 for double) |

**Example (explicit dimensions):**
```json
{
  "action": "resize",
  "image_url": "https://example.com/photo.png",
  "params": { "width": 256, "height": 256 }
}
```

**Example (scale factor):**
```json
{
  "action": "resize",
  "file_id": "abc123",
  "params": { "scale": 0.5 }
}
```

---

##### crop
Crop an image to a rectangular region.

**Required:** An image input + `box` in params
**Optional params:** None beyond the required box
| Param | Type | Description |
|-------|------|-------------|
| box | array of 4 ints | Crop region as `[left, top, right, bottom]` in pixels |

**Example:**
```json
{
  "action": "crop",
  "image_url": "https://example.com/photo.png",
  "params": { "box": [50, 50, 300, 300] }
}
```

---

##### rotate
Rotate an image by a specified number of degrees.

**Required:** An image input
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| degrees | float | 0 | Rotation angle in degrees (counter-clockwise) |
| expand | boolean | true | Expand canvas to fit rotated image |

**Example:**
```json
{
  "action": "rotate",
  "image_url": "https://example.com/photo.png",
  "params": { "degrees": 90 }
}
```

---

##### blur
Apply Gaussian blur to an image.

**Required:** An image input
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| radius | float | 2.0 | Blur radius (higher = more blur) |

**Example:**
```json
{
  "action": "blur",
  "file_id": "abc123",
  "params": { "radius": 5.0 }
}
```

---

##### border
Add a solid-color border around an image.

**Required:** An image input
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| size | integer | 10 | Border width in pixels |
| color | string/array | `"#000000"` | Border color |

**Example:**
```json
{
  "action": "border",
  "image_url": "https://example.com/photo.png",
  "params": { "size": 20, "color": "#0000ff" }
}
```

---

##### invert
Invert all colors in an image, producing a photographic negative effect. Each RGB pixel value is replaced with 255 minus its original value. Alpha transparency is preserved on RGBA images.

**Required:** An image input (image_url, image_base64, or file_id)
**Optional params:** None

**Example:**
```json
{
  "action": "invert",
  "image_url": "https://example.com/photo.png"
}
```

**Example (with file_id):**
```json
{
  "action": "invert",
  "file_id": "abc123",
  "output_format": "png",
  "store_file": true
}
```

---

##### text
Draw text onto an image.

**Required:** An image input + `text` in params
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| text | string | *(required)* | The text to draw |
| x | integer | 0 | X position in pixels |
| y | integer | 0 | Y position in pixels |
| size | integer | 20 | Font size |
| color | string/array | `"#000000"` | Text color |

**Example:**
```json
{
  "action": "text",
  "image_url": "https://example.com/photo.png",
  "params": { "text": "Hello World", "x": 50, "y": 100, "size": 36, "color": "#ffffff" }
}
```

---

##### draw
Draw shapes (line, rectangle, or ellipse) onto an image.

**Required:** An image input + `coordinates` in params
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| shape | string | `"line"` | Shape type: `line`, `rectangle`, or `ellipse` |
| coordinates | array | *(required)* | Coordinate pairs (e.g., `[x1, y1, x2, y2]`) |
| fill | string/array | `"#000000"` | Fill color |
| outline | string/array | `"#000000"` | Outline color (rectangle and ellipse) |
| width | integer | 1 | Line/outline width in pixels |

**Example (rectangle):**
```json
{
  "action": "draw",
  "image_url": "https://example.com/photo.png",
  "params": {
    "shape": "rectangle",
    "coordinates": [10, 10, 200, 150],
    "fill": "#ff000080",
    "outline": "#ff0000",
    "width": 3
  }
}
```

---

##### composite
Overlay one image on top of another with optional opacity.

**Required:** An image input (the base) + an overlay image via one of: `overlay_url`, `overlay_base64`, or `overlay_file_id` in params
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| overlay_url | string | — | URL of the overlay image |
| overlay_base64 | string | — | Base64-encoded overlay image |
| overlay_file_id | string | — | File ID of the overlay image |
| position | array | `[0, 0]` | `[x, y]` position to place the overlay |
| opacity | float | 1.0 | Overlay opacity (0.0 to 1.0) |

**Example:**
```json
{
  "action": "composite",
  "image_url": "https://example.com/background.png",
  "params": {
    "overlay_url": "https://example.com/logo.png",
    "position": [50, 50],
    "opacity": 0.8
  }
}
```

---

##### shear
Apply an affine shear transformation to an image.

**Required:** An image input
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| x | float | 0 | Horizontal shear factor |
| y | float | 0 | Vertical shear factor |

**Example:**
```json
{
  "action": "shear",
  "image_url": "https://example.com/photo.png",
  "params": { "x": 0.3, "y": 0.0 }
}
```

---

##### transparent
Make a specific color transparent in the image.

**Required:** An image input
**Optional params:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| color | string/array | `"#ffffff"` | The color to make transparent |

**Example:**
```json
{
  "action": "transparent",
  "image_url": "https://example.com/icon.png",
  "params": { "color": "#ffffff" },
  "output_format": "png"
}
```

---

##### multi_step
Chain multiple operations together in a single request. Each operation is applied sequentially.

**Required:** An image input (or use a `create` operation first) + `operations` array
**operations** is an array of objects, each with:
| Field | Type | Description |
|-------|------|-------------|
| action | string | Any single action listed above (not `multi_step` or `info`) |
| params | object | Parameters for that action |

**Example:**
```json
{
  "action": "multi_step",
  "image_url": "https://example.com/photo.png",
  "operations": [
    { "action": "resize", "params": { "width": 400, "height": 300 } },
    { "action": "invert", "params": {} },
    { "action": "border", "params": { "size": 5, "color": "#333333" } },
    { "action": "text", "params": { "text": "Inverted", "x": 10, "y": 10, "color": "#ffffff" } }
  ],
  "output_format": "jpeg",
  "filename": "processed.jpg"
}
```

---

#### Color Format
Colors can be specified as:
- Hex string: `"#RRGGBB"` or `"#RRGGBBAA"`
- RGB array: `[255, 0, 0]`
- RGBA array: `[255, 0, 0, 128]`
- Comma-separated string: `"255,0,0"` or `"255,0,0,128"`

#### Common Workflows

1. **Resize and watermark:** Use `multi_step` with `resize` then `text` to add a watermark label.
2. **Create branded image:** Use `create` to make a canvas, then `multi_step` with `composite` to overlay a logo and `text` for copy.
3. **Thumbnail generation:** Use `resize` with a `scale` factor or explicit small dimensions, output as `jpeg` for smaller file size.
4. **Remove white background:** Use `transparent` with `color: "#ffffff"` and output as `png` to preserve transparency.
5. **Annotate a screenshot:** Use `multi_step` with `draw` (rectangles for highlights) and `text` (labels).
6. **Create dark mode variant:** Use `invert` to flip all colors, useful for generating negative versions of light-themed assets.
7. **Accessibility contrast check:** Use `invert` to preview how content reads with reversed colors.

#### Important Notes
- Output is stored in cloud storage by default (store_file=true) and returns a `file_id` and `signed_url`.
- Use `file_id` from a previous result as input for follow-up edits.
- The `info` action returns dimensions and mode without producing an output image.
- The `create` action does not require any image input.
- For `multi_step`, operations are applied in order; each step modifies the image from the previous step.
- Inline base64 output (return_base64=true) is limited to 10 MB.
- Stored files expire after 7 days.

## When To Use
- Use this skill for `Image Editor` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: image editor, generating branded social media graphics by compositing logos onto product images, automating thumbnail creation by resizing and cropping uploaded images to standard dimensions, adding watermarks or copyright text overlays to protect visual content, creating placeholder images with custom colors and dimensions for ui mockups, blur, image base64, image url.
- Supported action names: `blur`, `border`, `composite`, `create`, `crop`, `draw`, `info`, `invert`, `multi_step`, `resize`, `rotate`, `shear`, `text`, `transparent`.

## Use Cases
- Generating branded social media graphics by compositing logos onto product images
- automating thumbnail creation by resizing and cropping uploaded images to standard dimensions
- adding watermarks or copyright text overlays to protect visual content
- creating placeholder images with custom colors and dimensions for UI mockups
- batch processing profile photos with consistent borders and formatting
- applying blur effects to sensitive regions before sharing screenshots
- building dynamic certificate or badge generators with text overlays
- removing white backgrounds from product images using transparency conversion
- preparing images for web optimization by converting formats and resizing for performance
- chaining multi-step edits to rotate
- crop
- resize
- and watermark images in a single automated workflow
- inverting image colors to create negative versions for dark mode assets or artistic effects
- generating high-contrast inverted previews for accessibility testing

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`)

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `14`.
x402 availability: not enabled for this product.

- `blur` (action slug: `blur`): Apply Gaussian blur to an image. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `border` (action slug: `border`): Add a solid-color border around an image. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `composite` (action slug: `composite`): Overlay one image on top of another with optional opacity. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `create` (action slug: `create`): Create a new blank image canvas with custom dimensions and background color. Price: `10` credits. Parameters: `filename`, `output_format`, `params`, `return_base64`, `store_file`.
- `crop` (action slug: `crop`): Crop an image to a rectangular region defined by [left, top, right, bottom] coordinates. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `draw` (action slug: `draw`): Draw shapes (line, rectangle, or ellipse) onto an image. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `info` (action slug: `info`): Get image dimensions and mode without modifying the image. Price: `10` credits. Parameters: `file_id`, `image_base64`, `image_url`.
- `invert` (action slug: `invert`): Invert all colors in an image, producing a photographic negative effect. Each RGB pixel value is replaced with 255 minus its original value. Alpha transparency is preserved. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `return_base64`, `store_file`.
- `multi_step` (action slug: `multi-step`): Chain multiple image operations together in a single request. Each operation is applied sequentially to the image. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `operations`, `output_format`, `return_base64`, `store_file`.
- `resize` (action slug: `resize`): Resize an image to specific dimensions or by a scale factor. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `rotate` (action slug: `rotate`): Rotate an image by a specified number of degrees (counter-clockwise). Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `shear` (action slug: `shear`): Apply an affine shear transformation to an image. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `text` (action slug: `text`): Draw text onto an image at a specified position with customizable size and color. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.
- `transparent` (action slug: `transparent`): Make a specific color transparent in the image. Output as PNG to preserve transparency. Price: `10` credits. Parameters: `file_id`, `filename`, `image_base64`, `image_url`, `output_format`, `params`, `return_base64`, `store_file`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "image-editor"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "image-editor"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "image-editor"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "image-editor"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "image-editor"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "image-editor"
  }
}
```

## Call This Tool
Product slug: `image-editor`

Marketplace page: https://www.agentpmt.com/marketplace/image-editor

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- x402 route: not enabled for this product.
- AgentPMT overview: use `../what-is-agentpmt` for marketplace, Agent Group, workflow, MCP, REST, and payment concepts.

If those setup skills are not installed beside this product skill, use the downloads below.

Core AgentPMT setup skills:
- What AgentPMT is: ../what-is-agentpmt
  - ClawHub page: https://clawhub.ai/agentpmt/what-is-agentpmt
  - OpenClaw install: `openclaw skills install what-is-agentpmt`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
  - OpenClaw install: `openclaw skills install agentpmt-account-mcp-rest-api-setup`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "Image-Editor",
    "arguments": {
      "action": "blur",
      "file_id": "example file id",
      "filename": "example filename",
      "image_base64": "example image base64",
      "image_url": "https://example.com",
      "output_format": "png",
      "params": {
        "radius": 2
      },
      "return_base64": false,
      "store_file": true
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "image-editor",
  "parameters": {
    "action": "blur",
    "file_id": "example file id",
    "filename": "example filename",
    "image_base64": "example image base64",
    "image_url": "https://example.com",
    "output_format": "png",
    "params": {
      "radius": 2
    },
    "return_base64": false,
    "store_file": true
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `blur` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/image-editor
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
