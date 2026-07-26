---
name: google-slides
description: "Google Slides: Create, edit, and manage Google Slides presentations. Add slides, text boxes, images, tables, and shapes. Use when an agent needs google slides, create presentations from scratch, add slides with predefined layouts, insert text boxes with styled content, embed images into slides, add image, presentation id, page object id through AgentPMT-hosted remote tool calls. Discovery terms: google slides, create presentations from scratch, add slides with predefined layouts."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-slides
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-slides"}}
---
# Google Slides

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Build stunning presentations without ever opening a browser. Create slide decks from scratch, add text, images, tables, and shapes, apply custom styles, fill templates with dynamic data, and generate slide thumbnails — all from your workflow. Perfect for automating reports, pitch decks, and client deliverables.

## Product Instructions
### Google Slides

Create, edit, and manage Google Slides presentations -- add slides, text, images, tables, shapes, apply styles, fill templates, and generate thumbnails.

#### Overview

This tool provides full access to the Google Slides API v1. You can create new presentations, add and arrange slides, insert text boxes, images, tables, and shapes, style text and shapes, perform template merges using placeholder tags, generate slide thumbnails, and execute raw batchUpdate requests for advanced operations. All position and size values use inches for convenience (internally converted to EMU at 914,400 EMU per inch).

#### Actions

##### create_presentation

Create a new empty Google Slides presentation.

**Required parameters:**
- `title` (string) -- title for the new presentation

**Example:**
```json
{"action":"create_presentation","title":"Q4 Revenue Report"}
```

Returns: `presentation_id`, `title`, `locale`, `slide_count`, `slides[]`, `page_size`

---

##### get_presentation

Retrieve full details of an existing presentation including all slides and elements.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID

**Example:**
```json
{"action":"get_presentation","presentation_id":"1BxiMVs0XRA5nFMdKvBdBZjgmUii9Op3a7eh"}
```

Returns: `presentation_id`, `title`, `locale`, `slide_count`, `slides[]` (with `object_id`, `layout`, `element_count`), `page_size`, `raw` (full API response)

---

##### search_presentations

Search for Google Slides presentations by name. Results are sorted by most recently modified.

**Optional parameters:**
- `query` (string) -- name contains match. If omitted, lists recent presentations
- `max_results` (integer, 1-100, default 20) -- maximum number of results

**Example -- search by name:**
```json
{"action":"search_presentations","query":"quarterly review"}
```

**Example -- list recent with limit:**
```json
{"action":"search_presentations","query":"Q4 report","max_results":5}
```

Returns: `query`, `result_count`, `presentations[]` (with `presentation_id`, `name`, `created_time`, `modified_time`, `owners[]`, `web_view_link`)

---

##### get_slide_thumbnail

Generate a PNG thumbnail image of a specific slide.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `page_object_id` (string) -- the slide/page object ID

**Optional parameters:**
- `thumbnail_size` (string) -- `LARGE` (1600px, default), `MEDIUM` (800px), or `SMALL` (200px)

**Example:**
```json
{"action":"get_slide_thumbnail","presentation_id":"1BxiMVs0XRA5","page_object_id":"g1234abcd"}
```

Returns: `content_url` (PNG URL, valid for approximately 30 minutes), `width`, `height`

---

##### add_slide

Add a new slide to a presentation.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID

**Optional parameters:**
- `insertion_index` (integer) -- 0-based position (default: appended at end)
- `layout` (string) -- predefined layout: `BLANK`, `TITLE`, `TITLE_AND_BODY`, `TITLE_AND_TWO_COLUMNS`, `TITLE_ONLY`, `SECTION_HEADER`, `SECTION_TITLE_AND_DESCRIPTION`, `ONE_COLUMN_TEXT`, `MAIN_POINT`, `BIG_NUMBER`, `CAPTION_ONLY`
- `object_id_value` (string) -- custom slide ID (auto-generated if omitted)

**Example:**
```json
{"action":"add_slide","presentation_id":"1BxiMVs0XRA5","layout":"TITLE_AND_BODY","insertion_index":1}
```

Returns: `presentation_id`, `created_slide_id`, `replies[]`

---

##### delete_object

Delete a slide or element from a presentation.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `object_id_value` (string) -- the slide or element ID to delete

**Example:**
```json
{"action":"delete_object","presentation_id":"1BxiMVs0XRA5","object_id_value":"g1234abcd"}
```

Returns: `presentation_id`, `deleted_object_id`, `replies[]`

---

##### add_text_box

Add a text box to a slide.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `page_object_id` (string) -- the target slide ID

**Optional parameters:**
- `text` (string) -- initial text content
- `element_properties` (object) -- position and size: `{x_inches, y_inches, width_inches, height_inches}` (defaults: 0, 0, 3, 1)
- `object_id_value` (string) -- custom element ID (auto-generated if omitted)

**Example:**
```json
{"action":"add_text_box","presentation_id":"1BxiMVs0XRA5","page_object_id":"g1234abcd","text":"Hello World","element_properties":{"x_inches":1,"y_inches":2,"width_inches":5,"height_inches":1}}
```

Returns: `presentation_id`, `created_text_box_id`, `replies[]`

---

##### add_image

Add an image to a slide.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `page_object_id` (string) -- the target slide ID
- `image_url` (string) -- publicly accessible image URL

**Optional parameters:**
- `element_properties` (object) -- position and size (defaults: 0, 0, 4, 3)
- `object_id_value` (string) -- custom element ID

**Example:**
```json
{"action":"add_image","presentation_id":"1BxiMVs0XRA5","page_object_id":"g1234abcd","image_url":"https://example.com/logo.png","element_properties":{"x_inches":2,"y_inches":1,"width_inches":4,"height_inches":3}}
```

Returns: `presentation_id`, `created_image_id`, `replies[]`

---

##### add_table

Add a table to a slide, optionally pre-populated with data.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `page_object_id` (string) -- the target slide ID
- `rows` (integer, 1-100) -- number of rows
- `columns` (integer, 1-20) -- number of columns

**Optional parameters:**
- `table_data` (array of arrays of strings) -- 2D array of cell text to populate after creation
- `object_id_value` (string) -- custom table ID

**Example:**
```json
{"action":"add_table","presentation_id":"1BxiMVs0XRA5","page_object_id":"g1234abcd","rows":3,"columns":4,"table_data":[["Name","Q1","Q2","Q3"],["Alice","100","200","300"],["Bob","150","250","350"]]}
```

Returns: `presentation_id`, `created_table_id`, `replies[]`

---

##### add_shape

Add a shape to a slide with optional text inside.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `page_object_id` (string) -- the target slide ID

**Optional parameters:**
- `shape_type` (string) -- `TEXT_BOX`, `RECTANGLE`, `ELLIPSE`, `ROUND_RECTANGLE`, `STAR_4`, `ARROW_EAST`, etc. (default: `RECTANGLE`)
- `text` (string) -- text content inside the shape
- `element_properties` (object) -- position and size (defaults: 0, 0, 2, 2)
- `object_id_value` (string) -- custom element ID

**Example:**
```json
{"action":"add_shape","presentation_id":"1BxiMVs0XRA5","page_object_id":"g1234abcd","shape_type":"ELLIPSE","element_properties":{"x_inches":3,"y_inches":2,"width_inches":2,"height_inches":2}}
```

Returns: `presentation_id`, `created_shape_id`, `replies[]`

---

##### insert_text

Insert text into an existing shape or table cell.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `object_id_value` (string) -- the shape or table object ID
- `text` (string) -- text to insert

**Optional parameters:**
- `text_insertion_index` (integer, default 0) -- character index for insertion
- `cell_location` (object) -- for table cells: `{"rowIndex": 0, "columnIndex": 0}`

**Example -- insert into shape:**
```json
{"action":"insert_text","presentation_id":"1BxiMVs0XRA5","object_id_value":"myShape1","text":"New text"}
```

**Example -- insert into table cell:**
```json
{"action":"insert_text","presentation_id":"1BxiMVs0XRA5","object_id_value":"myTable1","text":"Cell value","cell_location":{"rowIndex":1,"columnIndex":2}}
```

Returns: `presentation_id`, `replies[]`

---

##### replace_all_text

Find and replace text across the entire presentation. Ideal for template merging with `{{tag}}` placeholders.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `search_text` (string) -- text to find (e.g. a template tag)
- `replace_text` (string) -- replacement text

**Optional parameters:**
- `match_case` (boolean, default true) -- case-sensitive matching

**Example:**
```json
{"action":"replace_all_text","presentation_id":"1BxiMVs0XRA5","search_text":"{{customer_name}}","replace_text":"Acme Corp"}
```

Returns: `presentation_id`, `replies[]` (includes count of replacements)

---

##### replace_all_shapes_with_image

Replace all shapes containing specific text with an image. Useful for template image placeholders.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `search_text` (string) -- text in shapes to find (e.g. `{{logo}}`)
- `image_url` (string) -- publicly accessible image URL

**Optional parameters:**
- `image_replace_method` (string) -- `CENTER_INSIDE` (default) or `CENTER_CROP`
- `match_case` (boolean, default true) -- case-sensitive matching

**Example:**
```json
{"action":"replace_all_shapes_with_image","presentation_id":"1BxiMVs0XRA5","search_text":"{{logo}}","image_url":"https://example.com/logo.png"}
```

Returns: `presentation_id`, `replies[]`

---

##### update_text_style

Apply styling to text within a shape.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `object_id_value` (string) -- the shape containing the text
- `text_style` (object) -- style properties to apply. Available fields:
  - `bold` (boolean)
  - `italic` (boolean)
  - `underline` (boolean)
  - `font_family` (string)
  - `font_size_pt` (number) -- font size in points
  - `foreground_color_hex` (string) -- hex color, e.g. `#FF0000`
  - `link_url` (string) -- makes text a hyperlink

**Optional parameters:**
- `text_range_type` (string) -- `ALL` (default), `FIXED_RANGE`, or `FROM_START_INDEX`
- `start_index` (integer) -- start character index (for `FIXED_RANGE` or `FROM_START_INDEX`)
- `end_index` (integer) -- end character index (for `FIXED_RANGE`)

**Example:**
```json
{"action":"update_text_style","presentation_id":"1BxiMVs0XRA5","object_id_value":"myShape1","text_style":{"bold":true,"font_size_pt":24,"foreground_color_hex":"#0000FF"}}
```

**Example -- style a range of characters:**
```json
{"action":"update_text_style","presentation_id":"1BxiMVs0XRA5","object_id_value":"myShape1","text_style":{"italic":true,"link_url":"https://example.com"},"text_range_type":"FIXED_RANGE","start_index":0,"end_index":10}
```

Returns: `presentation_id`, `replies[]`

---

##### update_shape_properties

Update visual properties of a shape (fill color, outline).

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `object_id_value` (string) -- the shape element ID

**Optional parameters:**
- `shape_background_color_hex` (string) -- fill color hex
- `outline_color_hex` (string) -- outline color hex
- `outline_weight_pt` (number) -- outline weight in points

**Example:**
```json
{"action":"update_shape_properties","presentation_id":"1BxiMVs0XRA5","object_id_value":"myShape1","shape_background_color_hex":"#FFCC00","outline_color_hex":"#000000","outline_weight_pt":2}
```

Returns: `presentation_id`, `replies[]`

---

##### update_slide_properties

Update slide-level properties such as background color or skip-in-slideshow.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `page_object_id` (string) -- the slide ID

**Optional parameters:**
- `background_color_hex` (string) -- slide background color hex
- `skip_slide` (boolean) -- skip this slide during slideshow playback

**Example:**
```json
{"action":"update_slide_properties","presentation_id":"1BxiMVs0XRA5","page_object_id":"g1234abcd","background_color_hex":"#F5F5F5"}
```

Returns: `presentation_id`, `replies[]`

---

##### duplicate_object

Duplicate a slide or element within the presentation.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `object_id_value` (string) -- the slide or element ID to duplicate

**Example:**
```json
{"action":"duplicate_object","presentation_id":"1BxiMVs0XRA5","object_id_value":"g1234abcd"}
```

Returns: `presentation_id`, `replies[]` (includes new object ID)

---

##### reorder_slides

Move one or more slides to a new position.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `slide_object_ids` (array of strings) -- slide IDs to move
- `new_position` (integer) -- 0-based insertion index

**Example:**
```json
{"action":"reorder_slides","presentation_id":"1BxiMVs0XRA5","slide_object_ids":["slide1","slide2"],"new_position":0}
```

Returns: `presentation_id`, `replies[]`

---

##### batch_update

Execute raw Google Slides batchUpdate requests for advanced operations not covered by other actions. All requests execute atomically in order -- if one fails, none are applied.

**Required parameters:**
- `presentation_id` (string) -- the presentation ID
- `requests` (array of objects) -- raw Slides API request objects

**Example:**
```json
{"action":"batch_update","presentation_id":"1BxiMVs0XRA5","requests":[{"createSlide":{"objectId":"mySlide","slideLayoutReference":{"predefinedLayout":"BLANK"}}}]}
```

Returns: `presentation_id`, `replies[]`

---

#### Workflows

##### Template Merge Workflow

Fill a template presentation with dynamic data:

1. Create or identify a template presentation containing `{{tag}}` placeholders in text and shapes
2. Copy the template using the Google Drive tool (`copy_file` action) to preserve the original
3. Use `replace_all_text` for each text placeholder (e.g. `{{customer_name}}` to `Acme Corp`)
4. Use `replace_all_shapes_with_image` for each image placeholder (e.g. `{{logo}}` to an image URL)
5. The original template remains untouched

##### Build a Presentation from Scratch

1. `create_presentation` with a title
2. `add_slide` with desired layouts for each section
3. `add_text_box`, `add_image`, `add_table`, or `add_shape` to populate each slide
4. `update_text_style` and `update_shape_properties` to apply branding
5. `get_slide_thumbnail` to preview any slide

#### Notes

- Positions and sizes use inches. The API internally converts to EMU (914,400 EMU = 1 inch, 12,700 EMU = 1 point)
- Images must be publicly accessible URLs
- All batchUpdate-based actions are atomic -- if one operation in the batch fails, none are applied
- Object IDs are auto-generated if not provided. Use custom IDs (via `object_id_value`) when you need to reference elements in subsequent calls within the same session
- The `add_shape` action defaults to `RECTANGLE` shape type if `shape_type` is not specified (not `TEXT_BOX` -- use `add_text_box` for text boxes)
- Search results from `search_presentations` only return Google Slides files (filtered by MIME type)
- Thumbnail URLs from `get_slide_thumbnail` expire after approximately 30 minutes

## When To Use
- Use this skill for `Google Slides` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google slides, create presentations from scratch, add slides with predefined layouts, insert text boxes with styled content, embed images into slides, add image, presentation id, page object id.
- Supported action names: `add_image`, `add_shape`, `add_slide`, `add_table`, `add_text_box`, `batch_update`, `create_presentation`, `delete_object`, `duplicate_object`, `get_presentation`, `get_slide_thumbnail`, `insert_text`, `reorder_slides`, `replace_all_shapes_with_image`, `replace_all_text`, `search_presentations`, `update_shape_properties`, `update_slide_properties`, `update_text_style`.

## Use Cases
- Create presentations from scratch
- Add slides with predefined layouts
- Insert text boxes with styled content
- Embed images into slides
- Create data tables on slides
- Fill presentation templates with dynamic data
- Generate slide thumbnails
- Style text with fonts and colors
- Apply shape backgrounds and outlines
- Duplicate and reorder slides

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `19`.
x402 availability: not enabled for this product.

- `add_image` (action slug: `add-image`): Add an image to a slide. Price: `5` credits. Parameters: `element_properties`, `image_url`, `object_id_value`, `page_object_id`, `presentation_id`.
- `add_shape` (action slug: `add-shape`): Add a shape to a slide with optional text inside. Price: `5` credits. Parameters: `element_properties`, `object_id_value`, `page_object_id`, `presentation_id`, `shape_type`, `text`.
- `add_slide` (action slug: `add-slide`): Add a new slide to a presentation. Price: `5` credits. Parameters: `insertion_index`, `layout`, `object_id_value`, `presentation_id`.
- `add_table` (action slug: `add-table`): Add a table to a slide, optionally pre-populated with data. Price: `5` credits. Parameters: `columns`, `object_id_value`, `page_object_id`, `presentation_id`, `rows`, `table_data`.
- `add_text_box` (action slug: `add-text-box`): Add a text box to a slide. Price: `5` credits. Parameters: `element_properties`, `object_id_value`, `page_object_id`, `presentation_id`, `text`.
- `batch_update` (action slug: `batch-update`): Execute raw Google Slides batchUpdate requests for advanced operations. All requests execute atomically. Price: `5` credits. Parameters: `presentation_id`, `requests`.
- `create_presentation` (action slug: `create-presentation`): Create a new empty Google Slides presentation. Price: `5` credits. Parameters: `title`.
- `delete_object` (action slug: `delete-object`): Delete a slide or element from a presentation. Price: `5` credits. Parameters: `object_id_value`, `presentation_id`.
- `duplicate_object` (action slug: `duplicate-object`): Duplicate a slide or element within the presentation. Price: `5` credits. Parameters: `object_id_value`, `presentation_id`.
- `get_presentation` (action slug: `get-presentation`): Retrieve full details of an existing presentation including all slides and elements. Price: `5` credits. Parameters: `presentation_id`.
- `get_slide_thumbnail` (action slug: `get-slide-thumbnail`): Generate a PNG thumbnail image of a specific slide. Price: `5` credits. Parameters: `page_object_id`, `presentation_id`, `thumbnail_size`.
- `insert_text` (action slug: `insert-text`): Insert text into an existing shape or table cell. Price: `5` credits. Parameters: `cell_location`, `object_id_value`, `presentation_id`, `text`, `text_insertion_index`.
- `reorder_slides` (action slug: `reorder-slides`): Move one or more slides to a new position. Price: `5` credits. Parameters: `new_position`, `presentation_id`, `slide_object_ids`.
- `replace_all_shapes_with_image` (action slug: `replace-all-shapes-with-image`): Replace all shapes containing specific text with an image. Useful for template image placeholders. Price: `5` credits. Parameters: `image_replace_method`, `image_url`, `match_case`, `presentation_id`, `search_text`.
- `replace_all_text` (action slug: `replace-all-text`): Find and replace text across the entire presentation. Ideal for template merging with {{tag}} placeholders. Price: `5` credits. Parameters: `match_case`, `presentation_id`, `replace_text`, `search_text`.
- `search_presentations` (action slug: `search-presentations`): Search for Google Slides presentations by name. Results sorted by most recently modified. Price: `5` credits. Parameters: `max_results`, `query`.
- `update_shape_properties` (action slug: `update-shape-properties`): Update visual properties of a shape (fill color, outline). Price: `5` credits. Parameters: `object_id_value`, `outline_color_hex`, `outline_weight_pt`, `presentation_id`, `shape_background_color_hex`.
- `update_slide_properties` (action slug: `update-slide-properties`): Update slide-level properties such as background color or skip-in-slideshow. Price: `5` credits. Parameters: `background_color_hex`, `page_object_id`, `presentation_id`, `skip_slide`.
- `update_text_style` (action slug: `update-text-style`): Apply styling to text within a shape. Price: `5` credits. Parameters: `end_index`, `object_id_value`, `presentation_id`, `start_index`, `text_range_type`, `text_style`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-slides"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-slides"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-slides"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-slides"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-slides"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-slides"
  }
}
```

## Call This Tool
Product slug: `google-slides`

Marketplace page: https://www.agentpmt.com/marketplace/google-slides

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
    "name": "Google-Slides",
    "arguments": {
      "action": "add_image",
      "element_properties": {
        "height_inches": 3,
        "width_inches": 4,
        "x_inches": 0,
        "y_inches": 0
      },
      "image_url": "https://example.com",
      "object_id_value": "example object id value",
      "page_object_id": "example page object id",
      "presentation_id": "example presentation id"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-slides",
  "parameters": {
    "action": "add_image",
    "element_properties": {
      "height_inches": 3,
      "width_inches": 4,
      "x_inches": 0,
      "y_inches": 0
    },
    "image_url": "https://example.com",
    "object_id_value": "example object id value",
    "page_object_id": "example page object id",
    "presentation_id": "example presentation id"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `add_image` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-slides
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
