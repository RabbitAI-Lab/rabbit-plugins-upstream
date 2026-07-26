# Google Slides Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-slides`

x402 availability: not enabled for this product.

## `add_image`

Action slug: `add-image`

Price: `5` credits

Add an image to a slide.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `element_properties` | `object` | no | Position and size in inches |
| `image_url` | `string` | yes | Publicly accessible image URL |
| `object_id_value` | `string` | no | Custom element ID (auto-generated if omitted) |
| `page_object_id` | `string` | yes | Target slide ID |
| `presentation_id` | `string` | yes | Presentation ID |

Sample parameters:

```json
{
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
```

Generated JSON parameter schema:

```json
{
  "element_properties": {
    "description": "Position and size in inches",
    "properties": {
      "height_inches": {
        "default": 3,
        "description": "Height in inches",
        "required": false,
        "type": "number"
      },
      "width_inches": {
        "default": 4,
        "description": "Width in inches",
        "required": false,
        "type": "number"
      },
      "x_inches": {
        "default": 0,
        "description": "X position in inches",
        "required": false,
        "type": "number"
      },
      "y_inches": {
        "default": 0,
        "description": "Y position in inches",
        "required": false,
        "type": "number"
      }
    },
    "required": false,
    "type": "object"
  },
  "image_url": {
    "description": "Publicly accessible image URL",
    "required": true,
    "type": "string"
  },
  "object_id_value": {
    "description": "Custom element ID (auto-generated if omitted)",
    "required": false,
    "type": "string"
  },
  "page_object_id": {
    "description": "Target slide ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  }
}
```

## `add_shape`

Action slug: `add-shape`

Price: `5` credits

Add a shape to a slide with optional text inside.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `element_properties` | `object` | no | Position and size in inches |
| `object_id_value` | `string` | no | Custom element ID (auto-generated if omitted) |
| `page_object_id` | `string` | yes | Target slide ID |
| `presentation_id` | `string` | yes | Presentation ID |
| `shape_type` | `string` | no | Shape type: TEXT_BOX, RECTANGLE, ELLIPSE, ROUND_RECTANGLE, STAR_4, ARROW_EAST, etc. Default: RECTANGLE |
| `text` | `string` | no | Text content inside the shape |

Sample parameters:

```json
{
  "element_properties": {
    "height_inches": 2,
    "width_inches": 2,
    "x_inches": 0,
    "y_inches": 0
  },
  "object_id_value": "example object id value",
  "page_object_id": "example page object id",
  "presentation_id": "example presentation id",
  "shape_type": "RECTANGLE",
  "text": "example text"
}
```

Generated JSON parameter schema:

```json
{
  "element_properties": {
    "description": "Position and size in inches",
    "properties": {
      "height_inches": {
        "default": 2,
        "description": "Height in inches",
        "required": false,
        "type": "number"
      },
      "width_inches": {
        "default": 2,
        "description": "Width in inches",
        "required": false,
        "type": "number"
      },
      "x_inches": {
        "default": 0,
        "description": "X position in inches",
        "required": false,
        "type": "number"
      },
      "y_inches": {
        "default": 0,
        "description": "Y position in inches",
        "required": false,
        "type": "number"
      }
    },
    "required": false,
    "type": "object"
  },
  "object_id_value": {
    "description": "Custom element ID (auto-generated if omitted)",
    "required": false,
    "type": "string"
  },
  "page_object_id": {
    "description": "Target slide ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "shape_type": {
    "default": "RECTANGLE",
    "description": "Shape type: TEXT_BOX, RECTANGLE, ELLIPSE, ROUND_RECTANGLE, STAR_4, ARROW_EAST, etc. Default: RECTANGLE",
    "required": false,
    "type": "string"
  },
  "text": {
    "description": "Text content inside the shape",
    "required": false,
    "type": "string"
  }
}
```

## `add_slide`

Action slug: `add-slide`

Price: `5` credits

Add a new slide to a presentation.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `insertion_index` | `integer` | no | 0-based position to insert slide (default: appended at end) |
| `layout` | `string` | no | Predefined layout: BLANK, TITLE, TITLE_AND_BODY, TITLE_AND_TWO_COLUMNS, TITLE_ONLY, SECTION_HEADER, ONE_COLUMN_TEXT, MAIN_POINT, BIG_NUMBER, CAPTION_ONLY |
| `object_id_value` | `string` | no | Custom slide ID (auto-generated if omitted) |
| `presentation_id` | `string` | yes | Presentation ID |

Sample parameters:

```json
{
  "insertion_index": 1,
  "layout": "example layout",
  "object_id_value": "example object id value",
  "presentation_id": "example presentation id"
}
```

Generated JSON parameter schema:

```json
{
  "insertion_index": {
    "description": "0-based position to insert slide (default: appended at end)",
    "required": false,
    "type": "integer"
  },
  "layout": {
    "description": "Predefined layout: BLANK, TITLE, TITLE_AND_BODY, TITLE_AND_TWO_COLUMNS, TITLE_ONLY, SECTION_HEADER, ONE_COLUMN_TEXT, MAIN_POINT, BIG_NUMBER, CAPTION_ONLY",
    "required": false,
    "type": "string"
  },
  "object_id_value": {
    "description": "Custom slide ID (auto-generated if omitted)",
    "required": false,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  }
}
```

## `add_table`

Action slug: `add-table`

Price: `5` credits

Add a table to a slide, optionally pre-populated with data.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `columns` | `integer` | yes | Number of table columns |
| `object_id_value` | `string` | no | Custom table ID (auto-generated if omitted) |
| `page_object_id` | `string` | yes | Target slide ID |
| `presentation_id` | `string` | yes | Presentation ID |
| `rows` | `integer` | yes | Number of table rows |
| `table_data` | `array` | no | 2D array of cell text to populate after creation |

Sample parameters:

```json
{
  "columns": 1,
  "object_id_value": "example object id value",
  "page_object_id": "example page object id",
  "presentation_id": "example presentation id",
  "rows": 1,
  "table_data": [
    [
      "example table data"
    ]
  ]
}
```

Generated JSON parameter schema:

```json
{
  "columns": {
    "description": "Number of table columns",
    "maximum": 20,
    "minimum": 1,
    "required": true,
    "type": "integer"
  },
  "object_id_value": {
    "description": "Custom table ID (auto-generated if omitted)",
    "required": false,
    "type": "string"
  },
  "page_object_id": {
    "description": "Target slide ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "rows": {
    "description": "Number of table rows",
    "maximum": 100,
    "minimum": 1,
    "required": true,
    "type": "integer"
  },
  "table_data": {
    "description": "2D array of cell text to populate after creation",
    "items": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "required": false,
    "type": "array"
  }
}
```

## `add_text_box`

Action slug: `add-text-box`

Price: `5` credits

Add a text box to a slide.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `element_properties` | `object` | no | Position and size in inches |
| `object_id_value` | `string` | no | Custom element ID (auto-generated if omitted) |
| `page_object_id` | `string` | yes | Target slide ID |
| `presentation_id` | `string` | yes | Presentation ID |
| `text` | `string` | no | Initial text content |

Sample parameters:

```json
{
  "element_properties": {
    "height_inches": 1,
    "width_inches": 3,
    "x_inches": 0,
    "y_inches": 0
  },
  "object_id_value": "example object id value",
  "page_object_id": "example page object id",
  "presentation_id": "example presentation id",
  "text": "example text"
}
```

Generated JSON parameter schema:

```json
{
  "element_properties": {
    "description": "Position and size in inches",
    "properties": {
      "height_inches": {
        "default": 1,
        "description": "Height in inches",
        "required": false,
        "type": "number"
      },
      "width_inches": {
        "default": 3,
        "description": "Width in inches",
        "required": false,
        "type": "number"
      },
      "x_inches": {
        "default": 0,
        "description": "X position in inches from left edge",
        "required": false,
        "type": "number"
      },
      "y_inches": {
        "default": 0,
        "description": "Y position in inches from top edge",
        "required": false,
        "type": "number"
      }
    },
    "required": false,
    "type": "object"
  },
  "object_id_value": {
    "description": "Custom element ID (auto-generated if omitted)",
    "required": false,
    "type": "string"
  },
  "page_object_id": {
    "description": "Target slide ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "text": {
    "description": "Initial text content",
    "required": false,
    "type": "string"
  }
}
```

## `batch_update`

Action slug: `batch-update`

Price: `5` credits

Execute raw Google Slides batchUpdate requests for advanced operations. All requests execute atomically.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `presentation_id` | `string` | yes | Presentation ID |
| `requests` | `array` | yes | Raw Slides API request objects |

Sample parameters:

```json
{
  "presentation_id": "example presentation id",
  "requests": [
    {}
  ]
}
```

Generated JSON parameter schema:

```json
{
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "requests": {
    "description": "Raw Slides API request objects",
    "items": {
      "type": "object"
    },
    "required": true,
    "type": "array"
  }
}
```

## `create_presentation`

Action slug: `create-presentation`

Price: `5` credits

Create a new empty Google Slides presentation.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `title` | `string` | yes | Title for the new presentation |

Sample parameters:

```json
{
  "title": "example title"
}
```

Generated JSON parameter schema:

```json
{
  "title": {
    "description": "Title for the new presentation",
    "required": true,
    "type": "string"
  }
}
```

## `delete_object`

Action slug: `delete-object`

Price: `5` credits

Delete a slide or element from a presentation.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `object_id_value` | `string` | yes | Slide or element ID to delete |
| `presentation_id` | `string` | yes | Presentation ID |

Sample parameters:

```json
{
  "object_id_value": "example object id value",
  "presentation_id": "example presentation id"
}
```

Generated JSON parameter schema:

```json
{
  "object_id_value": {
    "description": "Slide or element ID to delete",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  }
}
```

## `duplicate_object`

Action slug: `duplicate-object`

Price: `5` credits

Duplicate a slide or element within the presentation.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `object_id_value` | `string` | yes | Slide or element ID to duplicate |
| `presentation_id` | `string` | yes | Presentation ID |

Sample parameters:

```json
{
  "object_id_value": "example object id value",
  "presentation_id": "example presentation id"
}
```

Generated JSON parameter schema:

```json
{
  "object_id_value": {
    "description": "Slide or element ID to duplicate",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  }
}
```

## `get_presentation`

Action slug: `get-presentation`

Price: `5` credits

Retrieve full details of an existing presentation including all slides and elements.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `presentation_id` | `string` | yes | Presentation ID |

Sample parameters:

```json
{
  "presentation_id": "example presentation id"
}
```

Generated JSON parameter schema:

```json
{
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  }
}
```

## `get_slide_thumbnail`

Action slug: `get-slide-thumbnail`

Price: `5` credits

Generate a PNG thumbnail image of a specific slide.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page_object_id` | `string` | yes | Slide/page object ID |
| `presentation_id` | `string` | yes | Presentation ID |
| `thumbnail_size` | `string` | no | Thumbnail size: LARGE (1600px), MEDIUM (800px), SMALL (200px) |

Sample parameters:

```json
{
  "page_object_id": "example page object id",
  "presentation_id": "example presentation id",
  "thumbnail_size": "LARGE"
}
```

Generated JSON parameter schema:

```json
{
  "page_object_id": {
    "description": "Slide/page object ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "thumbnail_size": {
    "default": "LARGE",
    "description": "Thumbnail size: LARGE (1600px), MEDIUM (800px), SMALL (200px)",
    "enum": [
      "LARGE",
      "MEDIUM",
      "SMALL"
    ],
    "required": false,
    "type": "string"
  }
}
```

## `insert_text`

Action slug: `insert-text`

Price: `5` credits

Insert text into an existing shape or table cell.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cell_location` | `object` | no | Table cell location for inserting into a table cell |
| `object_id_value` | `string` | yes | Shape or table object ID |
| `presentation_id` | `string` | yes | Presentation ID |
| `text` | `string` | yes | Text to insert |
| `text_insertion_index` | `integer` | no | Character index for insertion (default 0) |

Sample parameters:

```json
{
  "cell_location": {
    "columnIndex": 1,
    "rowIndex": 1
  },
  "object_id_value": "example object id value",
  "presentation_id": "example presentation id",
  "text": "example text",
  "text_insertion_index": 0
}
```

Generated JSON parameter schema:

```json
{
  "cell_location": {
    "description": "Table cell location for inserting into a table cell",
    "properties": {
      "columnIndex": {
        "description": "Column index (0-based)",
        "required": true,
        "type": "integer"
      },
      "rowIndex": {
        "description": "Row index (0-based)",
        "required": true,
        "type": "integer"
      }
    },
    "required": false,
    "type": "object"
  },
  "object_id_value": {
    "description": "Shape or table object ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "text": {
    "description": "Text to insert",
    "required": true,
    "type": "string"
  },
  "text_insertion_index": {
    "default": 0,
    "description": "Character index for insertion (default 0)",
    "required": false,
    "type": "integer"
  }
}
```

## `reorder_slides`

Action slug: `reorder-slides`

Price: `5` credits

Move one or more slides to a new position.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `new_position` | `integer` | yes | 0-based insertion index |
| `presentation_id` | `string` | yes | Presentation ID |
| `slide_object_ids` | `array` | yes | Slide IDs to move |

Sample parameters:

```json
{
  "new_position": 1,
  "presentation_id": "example presentation id",
  "slide_object_ids": [
    "example slide object id"
  ]
}
```

Generated JSON parameter schema:

```json
{
  "new_position": {
    "description": "0-based insertion index",
    "required": true,
    "type": "integer"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "slide_object_ids": {
    "description": "Slide IDs to move",
    "items": {
      "type": "string"
    },
    "required": true,
    "type": "array"
  }
}
```

## `replace_all_shapes_with_image`

Action slug: `replace-all-shapes-with-image`

Price: `5` credits

Replace all shapes containing specific text with an image. Useful for template image placeholders.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `image_replace_method` | `string` | no | How to fit image: CENTER_INSIDE (default) or CENTER_CROP |
| `image_url` | `string` | yes | Publicly accessible image URL |
| `match_case` | `boolean` | no | Case-sensitive matching (default true) |
| `presentation_id` | `string` | yes | Presentation ID |
| `search_text` | `string` | yes | Text in shapes to find (e.g. {{logo}}) |

Sample parameters:

```json
{
  "image_replace_method": "CENTER_INSIDE",
  "image_url": "https://example.com",
  "match_case": true,
  "presentation_id": "example presentation id",
  "search_text": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "image_replace_method": {
    "default": "CENTER_INSIDE",
    "description": "How to fit image: CENTER_INSIDE (default) or CENTER_CROP",
    "enum": [
      "CENTER_INSIDE",
      "CENTER_CROP"
    ],
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Publicly accessible image URL",
    "required": true,
    "type": "string"
  },
  "match_case": {
    "default": true,
    "description": "Case-sensitive matching (default true)",
    "required": false,
    "type": "boolean"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "search_text": {
    "description": "Text in shapes to find (e.g. {{logo}})",
    "required": true,
    "type": "string"
  }
}
```

## `replace_all_text`

Action slug: `replace-all-text`

Price: `5` credits

Find and replace text across the entire presentation. Ideal for template merging with {{tag}} placeholders.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `match_case` | `boolean` | no | Case-sensitive matching (default true) |
| `presentation_id` | `string` | yes | Presentation ID |
| `replace_text` | `string` | yes | Replacement text |
| `search_text` | `string` | yes | Text to find (e.g. a template tag like {{customer_name}}) |

Sample parameters:

```json
{
  "match_case": true,
  "presentation_id": "example presentation id",
  "replace_text": "example replace text",
  "search_text": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "match_case": {
    "default": true,
    "description": "Case-sensitive matching (default true)",
    "required": false,
    "type": "boolean"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "replace_text": {
    "description": "Replacement text",
    "required": true,
    "type": "string"
  },
  "search_text": {
    "description": "Text to find (e.g. a template tag like {{customer_name}})",
    "required": true,
    "type": "string"
  }
}
```

## `search_presentations`

Action slug: `search-presentations`

Price: `5` credits

Search for Google Slides presentations by name. Results sorted by most recently modified.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `max_results` | `integer` | no | Maximum number of results (1-100, default 20) |
| `query` | `string` | no | Name contains match. If omitted, lists recent presentations. |

Sample parameters:

```json
{
  "max_results": 20,
  "query": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "max_results": {
    "default": 20,
    "description": "Maximum number of results (1-100, default 20)",
    "maximum": 100,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "query": {
    "description": "Name contains match. If omitted, lists recent presentations.",
    "required": false,
    "type": "string"
  }
}
```

## `update_shape_properties`

Action slug: `update-shape-properties`

Price: `5` credits

Update visual properties of a shape (fill color, outline).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `object_id_value` | `string` | yes | Shape element ID |
| `outline_color_hex` | `string` | no | Outline color hex |
| `outline_weight_pt` | `number` | no | Outline weight in points |
| `presentation_id` | `string` | yes | Presentation ID |
| `shape_background_color_hex` | `string` | no | Fill color hex |

Sample parameters:

```json
{
  "object_id_value": "example object id value",
  "outline_color_hex": "example outline color hex",
  "outline_weight_pt": 1,
  "presentation_id": "example presentation id",
  "shape_background_color_hex": "example shape background color hex"
}
```

Generated JSON parameter schema:

```json
{
  "object_id_value": {
    "description": "Shape element ID",
    "required": true,
    "type": "string"
  },
  "outline_color_hex": {
    "description": "Outline color hex",
    "required": false,
    "type": "string"
  },
  "outline_weight_pt": {
    "description": "Outline weight in points",
    "required": false,
    "type": "number"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "shape_background_color_hex": {
    "description": "Fill color hex",
    "required": false,
    "type": "string"
  }
}
```

## `update_slide_properties`

Action slug: `update-slide-properties`

Price: `5` credits

Update slide-level properties such as background color or skip-in-slideshow.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `background_color_hex` | `string` | no | Slide background color hex |
| `page_object_id` | `string` | yes | Slide ID |
| `presentation_id` | `string` | yes | Presentation ID |
| `skip_slide` | `boolean` | no | Skip this slide during slideshow playback |

Sample parameters:

```json
{
  "background_color_hex": "example background color hex",
  "page_object_id": "example page object id",
  "presentation_id": "example presentation id",
  "skip_slide": true
}
```

Generated JSON parameter schema:

```json
{
  "background_color_hex": {
    "description": "Slide background color hex",
    "required": false,
    "type": "string"
  },
  "page_object_id": {
    "description": "Slide ID",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "skip_slide": {
    "description": "Skip this slide during slideshow playback",
    "required": false,
    "type": "boolean"
  }
}
```

## `update_text_style`

Action slug: `update-text-style`

Price: `5` credits

Apply styling to text within a shape.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `end_index` | `integer` | no | End character index (for FIXED_RANGE) |
| `object_id_value` | `string` | yes | Shape containing the text |
| `presentation_id` | `string` | yes | Presentation ID |
| `start_index` | `integer` | no | Start character index (for FIXED_RANGE or FROM_START_INDEX) |
| `text_range_type` | `string` | no | Which text to style: ALL (default), FIXED_RANGE, or FROM_START_INDEX |
| `text_style` | `object` | yes | Text style properties to apply |

Sample parameters:

```json
{
  "end_index": 1,
  "object_id_value": "example object id value",
  "presentation_id": "example presentation id",
  "start_index": 1,
  "text_range_type": "ALL",
  "text_style": {
    "bold": true,
    "font_family": "example font family",
    "font_size_pt": 1,
    "foreground_color_hex": "example foreground color hex",
    "italic": true,
    "link_url": "https://example.com",
    "underline": true
  }
}
```

Generated JSON parameter schema:

```json
{
  "end_index": {
    "description": "End character index (for FIXED_RANGE)",
    "required": false,
    "type": "integer"
  },
  "object_id_value": {
    "description": "Shape containing the text",
    "required": true,
    "type": "string"
  },
  "presentation_id": {
    "description": "Presentation ID",
    "required": true,
    "type": "string"
  },
  "start_index": {
    "description": "Start character index (for FIXED_RANGE or FROM_START_INDEX)",
    "required": false,
    "type": "integer"
  },
  "text_range_type": {
    "default": "ALL",
    "description": "Which text to style: ALL (default), FIXED_RANGE, or FROM_START_INDEX",
    "enum": [
      "ALL",
      "FIXED_RANGE",
      "FROM_START_INDEX"
    ],
    "required": false,
    "type": "string"
  },
  "text_style": {
    "description": "Text style properties to apply",
    "properties": {
      "bold": {
        "description": "Bold text",
        "required": false,
        "type": "boolean"
      },
      "font_family": {
        "description": "Font family name",
        "required": false,
        "type": "string"
      },
      "font_size_pt": {
        "description": "Font size in points",
        "required": false,
        "type": "number"
      },
      "foreground_color_hex": {
        "description": "Hex color e.g. #FF0000",
        "required": false,
        "type": "string"
      },
      "italic": {
        "description": "Italic text",
        "required": false,
        "type": "boolean"
      },
      "link_url": {
        "description": "Makes text a hyperlink",
        "required": false,
        "type": "string"
      },
      "underline": {
        "description": "Underline text",
        "required": false,
        "type": "boolean"
      }
    },
    "required": true,
    "type": "object"
  }
}
```
