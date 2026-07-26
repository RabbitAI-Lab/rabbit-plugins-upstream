# Image Editor Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `image-editor`

x402 availability: not enabled for this product.

## `blur`

Action slug: `blur`

Price: `10` credits

Apply Gaussian blur to an image.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image stored in cloud storage. |
| `filename` | `string` | no | Filename for stored output. Defaults to edited.<ext>. |
| `image_base64` | `string` | no | Base64-encoded image input (png, jpg, webp). |
| `image_url` | `string` | no | Public URL to an image (png, jpg, webp). |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | no | Blur parameters. Includes 'radius' (float, default 2.0). |
| `return_base64` | `boolean` | no | Return base64 output inline when size permits (max 10MB). |
| `store_file` | `boolean` | no | Store output in cloud storage for file management access. |

Sample parameters:

```json
{
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
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image stored in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output. Defaults to edited.<ext>.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input (png, jpg, webp).",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image (png, jpg, webp).",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Blur parameters. Includes 'radius' (float, default 2.0).",
    "properties": {
      "radius": {
        "default": 2,
        "description": "Blur radius (higher = more blur).",
        "required": false,
        "type": "number"
      }
    },
    "required": false,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline when size permits (max 10MB).",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage for file management access.",
    "required": false,
    "type": "boolean"
  }
}
```

## `border`

Action slug: `border`

Price: `10` credits

Add a solid-color border around an image.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image stored in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input (png, jpg, webp). |
| `image_url` | `string` | no | Public URL to an image (png, jpg, webp). |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | no | Border parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline when size permits. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "color": "#000000",
    "size": 10
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image stored in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input (png, jpg, webp).",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image (png, jpg, webp).",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Border parameters.",
    "properties": {
      "color": {
        "default": "#000000",
        "description": "Border color (hex string like '#000000', RGB array, or RGBA array).",
        "required": false,
        "type": "string"
      },
      "size": {
        "default": 10,
        "description": "Border width in pixels.",
        "required": false,
        "type": "integer"
      }
    },
    "required": false,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline when size permits.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `composite`

Action slug: `composite`

Price: `10` credits

Overlay one image on top of another with optional opacity.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of the base image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded base image input. |
| `image_url` | `string` | no | Public URL to the base image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | yes | Composite parameters. Provide overlay via overlay_url, overlay_base64, or overlay_file_id. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "opacity": 1,
    "overlay_base64": "example overlay base64",
    "overlay_file_id": "example overlay file id",
    "overlay_url": "https://example.com",
    "position": [
      0,
      0
    ]
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of the base image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded base image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to the base image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Composite parameters. Provide overlay via overlay_url, overlay_base64, or overlay_file_id.",
    "properties": {
      "opacity": {
        "default": 1,
        "description": "Overlay opacity (0.0 to 1.0).",
        "required": false,
        "type": "number"
      },
      "overlay_base64": {
        "description": "Base64-encoded overlay image.",
        "required": false,
        "type": "string"
      },
      "overlay_file_id": {
        "description": "File ID of the overlay image.",
        "required": false,
        "type": "string"
      },
      "overlay_url": {
        "description": "URL of the overlay image.",
        "required": false,
        "type": "string"
      },
      "position": {
        "default": [
          0,
          0
        ],
        "description": "[x, y] position to place the overlay.",
        "items": {
          "type": "integer"
        },
        "required": false,
        "type": "array"
      }
    },
    "required": true,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `create`

Action slug: `create`

Price: `10` credits

Create a new blank image canvas with custom dimensions and background color.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filename` | `string` | no | Filename for stored output. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | no | Canvas creation parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "filename": "example filename",
  "output_format": "png",
  "params": {
    "color": "#ffffff",
    "height": 512,
    "width": 512
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Canvas creation parameters.",
    "properties": {
      "color": {
        "default": "#ffffff",
        "description": "Fill color (hex string, RGB array, or RGBA array).",
        "required": false,
        "type": "string"
      },
      "height": {
        "default": 512,
        "description": "Canvas height in pixels.",
        "required": false,
        "type": "integer"
      },
      "width": {
        "default": 512,
        "description": "Canvas width in pixels.",
        "required": false,
        "type": "integer"
      }
    },
    "required": false,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `crop`

Action slug: `crop`

Price: `10` credits

Crop an image to a rectangular region defined by [left, top, right, bottom] coordinates.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | yes | Crop parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "box": [
      1
    ]
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Crop parameters.",
    "properties": {
      "box": {
        "description": "Crop region as [left, top, right, bottom] in pixels.",
        "items": {
          "type": "integer"
        },
        "required": true,
        "type": "array"
      }
    },
    "required": true,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `draw`

Action slug: `draw`

Price: `10` credits

Draw shapes (line, rectangle, or ellipse) onto an image.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | yes | Draw parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "coordinates": [
      1
    ],
    "fill": "#000000",
    "outline": "#000000",
    "shape": "line",
    "width": 1
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Draw parameters.",
    "properties": {
      "coordinates": {
        "description": "Coordinate pairs (e.g., [x1, y1, x2, y2]).",
        "items": {
          "type": "integer"
        },
        "required": true,
        "type": "array"
      },
      "fill": {
        "default": "#000000",
        "description": "Fill color (hex, RGB, or RGBA).",
        "required": false,
        "type": "string"
      },
      "outline": {
        "default": "#000000",
        "description": "Outline color for rectangle and ellipse.",
        "required": false,
        "type": "string"
      },
      "shape": {
        "default": "line",
        "description": "Shape type to draw.",
        "enum": [
          "line",
          "rectangle",
          "ellipse"
        ],
        "required": false,
        "type": "string"
      },
      "width": {
        "default": 1,
        "description": "Line/outline width in pixels.",
        "required": false,
        "type": "integer"
      }
    },
    "required": true,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `info`

Action slug: `info`

Price: `10` credits

Get image dimensions and mode without modifying the image.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "image_base64": "example image base64",
  "image_url": "https://example.com"
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  }
}
```

## `invert`

Action slug: `invert`

Price: `10` credits

Invert all colors in an image, producing a photographic negative effect. Each RGB pixel value is replaced with 255 minus its original value. Alpha transparency is preserved.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image stored in cloud storage. |
| `filename` | `string` | no | Filename for stored output. Defaults to edited.<ext>. |
| `image_base64` | `string` | no | Base64-encoded image input (png, jpg, webp). |
| `image_url` | `string` | no | Public URL to an image (png, jpg, webp). |
| `output_format` | `string` | no | Output image format. |
| `return_base64` | `boolean` | no | Return base64 output inline when size permits (max 10MB). |
| `store_file` | `boolean` | no | Store output in cloud storage for file management access. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image stored in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output. Defaults to edited.<ext>.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input (png, jpg, webp).",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image (png, jpg, webp).",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline when size permits (max 10MB).",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage for file management access.",
    "required": false,
    "type": "boolean"
  }
}
```

## `multi_step`

Action slug: `multi-step`

Price: `10` credits

Chain multiple image operations together in a single request. Each operation is applied sequentially to the image.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `operations` | `array` | yes | List of operations to apply sequentially. Each object has 'action' (string) and 'params' (object). |
| `output_format` | `string` | no | Output image format. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "operations": [
    {
      "action": "example action",
      "params": {}
    }
  ],
  "output_format": "png",
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "operations": {
    "description": "List of operations to apply sequentially. Each object has 'action' (string) and 'params' (object).",
    "items": {
      "properties": {
        "action": {
          "description": "Operation to perform: blur, border, composite, create, crop, draw, invert, resize, rotate, shear, text, transparent.",
          "required": true,
          "type": "string"
        },
        "params": {
          "description": "Parameters for this operation.",
          "required": false,
          "type": "object"
        }
      },
      "type": "object"
    },
    "required": true,
    "type": "array"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `resize`

Action slug: `resize`

Price: `10` credits

Resize an image to specific dimensions or by a scale factor.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | yes | Resize parameters. Provide width+height or scale. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "height": 1,
    "scale": 1,
    "width": 1
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Resize parameters. Provide width+height or scale.",
    "properties": {
      "height": {
        "description": "Target height in pixels.",
        "required": false,
        "type": "integer"
      },
      "scale": {
        "description": "Scale factor (e.g., 0.5 for half size, 2.0 for double).",
        "required": false,
        "type": "number"
      },
      "width": {
        "description": "Target width in pixels.",
        "required": false,
        "type": "integer"
      }
    },
    "required": true,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `rotate`

Action slug: `rotate`

Price: `10` credits

Rotate an image by a specified number of degrees (counter-clockwise).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | no | Rotation parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "degrees": 0,
    "expand": true
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Rotation parameters.",
    "properties": {
      "degrees": {
        "default": 0,
        "description": "Rotation angle in degrees (counter-clockwise).",
        "required": false,
        "type": "number"
      },
      "expand": {
        "default": true,
        "description": "Expand canvas to fit rotated image.",
        "required": false,
        "type": "boolean"
      }
    },
    "required": false,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `shear`

Action slug: `shear`

Price: `10` credits

Apply an affine shear transformation to an image.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | no | Shear parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "x": 0,
    "y": 0
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Shear parameters.",
    "properties": {
      "x": {
        "default": 0,
        "description": "Horizontal shear factor.",
        "required": false,
        "type": "number"
      },
      "y": {
        "default": 0,
        "description": "Vertical shear factor.",
        "required": false,
        "type": "number"
      }
    },
    "required": false,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `text`

Action slug: `text`

Price: `10` credits

Draw text onto an image at a specified position with customizable size and color.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. |
| `params` | `object` | yes | Text parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "color": "#000000",
    "size": 20,
    "text": "example text",
    "x": 0,
    "y": 0
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Text parameters.",
    "properties": {
      "color": {
        "default": "#000000",
        "description": "Text color (hex, RGB, or RGBA).",
        "required": false,
        "type": "string"
      },
      "size": {
        "default": 20,
        "description": "Font size.",
        "required": false,
        "type": "integer"
      },
      "text": {
        "description": "The text content to draw on the image.",
        "required": true,
        "type": "string"
      },
      "x": {
        "default": 0,
        "description": "X position in pixels.",
        "required": false,
        "type": "integer"
      },
      "y": {
        "default": 0,
        "description": "Y position in pixels.",
        "required": false,
        "type": "integer"
      }
    },
    "required": true,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```

## `transparent`

Action slug: `transparent`

Price: `10` credits

Make a specific color transparent in the image. Output as PNG to preserve transparency.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | File ID of an image in cloud storage. |
| `filename` | `string` | no | Filename for stored output. |
| `image_base64` | `string` | no | Base64-encoded image input. |
| `image_url` | `string` | no | Public URL to an image. |
| `output_format` | `string` | no | Output image format. Use 'png' to preserve transparency. |
| `params` | `object` | no | Transparency parameters. |
| `return_base64` | `boolean` | no | Return base64 output inline. |
| `store_file` | `boolean` | no | Store output in cloud storage. |

Sample parameters:

```json
{
  "file_id": "example file id",
  "filename": "example filename",
  "image_base64": "example image base64",
  "image_url": "https://example.com",
  "output_format": "png",
  "params": {
    "color": "#ffffff"
  },
  "return_base64": false,
  "store_file": true
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "File ID of an image in cloud storage.",
    "required": false,
    "type": "string"
  },
  "filename": {
    "description": "Filename for stored output.",
    "required": false,
    "type": "string"
  },
  "image_base64": {
    "description": "Base64-encoded image input.",
    "required": false,
    "type": "string"
  },
  "image_url": {
    "description": "Public URL to an image.",
    "required": false,
    "type": "string"
  },
  "output_format": {
    "default": "png",
    "description": "Output image format. Use 'png' to preserve transparency.",
    "enum": [
      "png",
      "jpeg",
      "webp"
    ],
    "required": false,
    "type": "string"
  },
  "params": {
    "description": "Transparency parameters.",
    "properties": {
      "color": {
        "default": "#ffffff",
        "description": "The color to make transparent (hex string, RGB array, or RGBA array).",
        "required": false,
        "type": "string"
      }
    },
    "required": false,
    "type": "object"
  },
  "return_base64": {
    "default": false,
    "description": "Return base64 output inline.",
    "required": false,
    "type": "boolean"
  },
  "store_file": {
    "default": true,
    "description": "Store output in cloud storage.",
    "required": false,
    "type": "boolean"
  }
}
```
