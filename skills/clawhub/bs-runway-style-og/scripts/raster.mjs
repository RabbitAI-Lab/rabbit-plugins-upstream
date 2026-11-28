const PNG_SIGNATURE = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);

export const MIME_BY_RASTER_FORMAT = new Map([
  ['webp', 'image/webp'],
  ['png', 'image/png'],
  ['jpeg', 'image/jpeg'],
]);

export const PRESET_DIMENSIONS = new Map([
  ['square_hd', { width: 1024, height: 1024 }],
  ['square', { width: 512, height: 512 }],
  ['portrait_4_3', { width: 768, height: 1024 }],
  ['portrait_16_9', { width: 576, height: 1024 }],
  ['landscape_4_3', { width: 1024, height: 768 }],
  ['landscape_16_9', { width: 1024, height: 576 }],
]);

function readUnsigned24LE(buffer, offset) {
  return buffer[offset] | (buffer[offset + 1] << 8) | (buffer[offset + 2] << 16);
}

function parsePng(buffer) {
  if (buffer.length < 45 || !buffer.subarray(0, 8).equals(PNG_SIGNATURE)) {
    return null;
  }
  let offset = 8;
  let width = null;
  let height = null;
  let sawIdat = false;
  let sawIend = false;
  let chunkIndex = 0;
  while (offset + 12 <= buffer.length) {
    const length = buffer.readUInt32BE(offset);
    const type = buffer.toString('ascii', offset + 4, offset + 8);
    const data = offset + 8;
    const end = data + length;
    if (end + 4 > buffer.length) throw new Error('PNG contains a truncated chunk.');
    if (chunkIndex === 0) {
      if (type !== 'IHDR' || length !== 13) {
        throw new Error('PNG must begin with a 13-byte IHDR chunk.');
      }
      width = buffer.readUInt32BE(data);
      height = buffer.readUInt32BE(data + 4);
      const bitDepth = buffer[data + 8];
      const colorType = buffer[data + 9];
      const validDepths = new Map([
        [0, new Set([1, 2, 4, 8, 16])],
        [2, new Set([8, 16])],
        [3, new Set([1, 2, 4, 8])],
        [4, new Set([8, 16])],
        [6, new Set([8, 16])],
      ]);
      if (!validDepths.get(colorType)?.has(bitDepth)) {
        throw new Error('PNG IHDR uses an invalid color type or bit depth.');
      }
      if (buffer[data + 10] !== 0 || buffer[data + 11] !== 0 || buffer[data + 12] > 1) {
        throw new Error('PNG IHDR uses unsupported compression, filter, or interlace fields.');
      }
    }
    if (type === 'IDAT') sawIdat = true;
    if (type === 'IEND') {
      if (length !== 0) throw new Error('PNG IEND chunk must be empty.');
      sawIend = true;
      offset = end + 4;
      break;
    }
    offset = end + 4;
    chunkIndex += 1;
  }
  if (!sawIdat || !sawIend || offset !== buffer.length) {
    throw new Error('PNG must contain complete IDAT and terminal IEND chunks.');
  }
  return { format: 'png', width, height };
}

function parseJpeg(buffer) {
  if (buffer.length < 16 || buffer[0] !== 0xff || buffer[1] !== 0xd8) return null;
  if (buffer[buffer.length - 2] !== 0xff || buffer[buffer.length - 1] !== 0xd9) {
    throw new Error('JPEG is missing its terminal end marker.');
  }
  const startOfFrame = new Set([
    0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
    0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf,
  ]);
  let offset = 2;
  while (offset + 4 <= buffer.length) {
    while (offset < buffer.length && buffer[offset] !== 0xff) offset += 1;
    while (offset < buffer.length && buffer[offset] === 0xff) offset += 1;
    if (offset >= buffer.length) break;
    const marker = buffer[offset];
    offset += 1;
    if (marker === 0xd8 || marker === 0xd9 || marker === 0x01) continue;
    if (marker >= 0xd0 && marker <= 0xd7) continue;
    if (offset + 2 > buffer.length) break;
    const length = buffer.readUInt16BE(offset);
    if (length < 2 || offset + length > buffer.length) {
      throw new Error('JPEG contains a truncated marker segment.');
    }
    if (startOfFrame.has(marker) && length >= 7) {
      const width = buffer.readUInt16BE(offset + 5);
      const height = buffer.readUInt16BE(offset + 3);
      return { format: 'jpeg', width, height };
    }
    if (marker === 0xda) break;
    offset += length;
  }
  throw new Error('JPEG dimensions could not be parsed before image data.');
}

function parseWebp(buffer) {
  if (
    buffer.length < 20 ||
    buffer.toString('ascii', 0, 4) !== 'RIFF' ||
    buffer.toString('ascii', 8, 12) !== 'WEBP'
  ) {
    return null;
  }
  if (buffer.readUInt32LE(4) + 8 !== buffer.length) {
    throw new Error('WebP RIFF length does not match the file length.');
  }

  let offset = 12;
  let canvas = null;
  let bitstream = null;
  let imageChunks = 0;
  while (offset + 8 <= buffer.length) {
    const type = buffer.toString('ascii', offset, offset + 4);
    const size = buffer.readUInt32LE(offset + 4);
    const data = offset + 8;
    const end = data + size;
    if (end > buffer.length) throw new Error('WebP contains a truncated chunk.');

    if (type === 'VP8X') {
      if (size !== 10 || canvas) throw new Error('WebP has an invalid VP8X chunk.');
      if ((buffer[data] & 0x02) !== 0) {
        throw new Error('Animated WebP is not supported for this output.');
      }
      canvas = {
        width: readUnsigned24LE(buffer, data + 4) + 1,
        height: readUnsigned24LE(buffer, data + 7) + 1,
      };
    }
    if (type === 'ANIM' || type === 'ANMF') {
      throw new Error('Animated WebP is not supported for this output.');
    }
    if (type === 'VP8L') {
      if (size < 5 || buffer[data] !== 0x2f) {
        throw new Error('WebP has an invalid VP8L bitstream.');
      }
      const bits = buffer.readUInt32LE(data + 1);
      bitstream = {
        width: (bits & 0x3fff) + 1,
        height: ((bits >> 14) & 0x3fff) + 1,
      };
      imageChunks += 1;
    }
    if (type === 'VP8 ') {
      if (
        size < 10 ||
        buffer[data + 3] !== 0x9d ||
        buffer[data + 4] !== 0x01 ||
        buffer[data + 5] !== 0x2a
      ) {
        throw new Error('WebP has an invalid VP8 frame header.');
      }
      bitstream = {
        width: buffer.readUInt16LE(data + 6) & 0x3fff,
        height: buffer.readUInt16LE(data + 8) & 0x3fff,
      };
      imageChunks += 1;
    }
    offset = end + (size % 2);
  }
  if (offset !== buffer.length || imageChunks !== 1 || !bitstream) {
    throw new Error('WebP must contain exactly one complete image bitstream.');
  }
  if (
    canvas &&
    (canvas.width !== bitstream.width || canvas.height !== bitstream.height)
  ) {
    throw new Error('WebP canvas dimensions do not match its image bitstream.');
  }
  return { format: 'webp', ...(canvas ?? bitstream) };
}

export function inspectRasterBytes(input, options = {}) {
  const buffer = Buffer.isBuffer(input) ? input : Buffer.from(input);
  const maxBytes = options.maxBytes ?? 32 * 1024 * 1024;
  if (buffer.length === 0) throw new Error('Raster file is empty.');
  if (buffer.length > maxBytes) {
    throw new Error(`Raster file exceeds the ${maxBytes}-byte safety limit.`);
  }
  const metadata = parsePng(buffer) ?? parseJpeg(buffer) ?? parseWebp(buffer);
  if (!metadata) throw new Error('Unsupported or invalid PNG, JPEG, or WebP file.');
  if (
    !Number.isInteger(metadata.width) ||
    !Number.isInteger(metadata.height) ||
    metadata.width <= 0 ||
    metadata.height <= 0 ||
    metadata.width > 16384 ||
    metadata.height > 16384
  ) {
    throw new Error('Raster dimensions are invalid or exceed 16384 pixels.');
  }
  return { ...metadata, bytes: buffer.length };
}
