"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.removeVideoWatermark = removeVideoWatermark;
const validator_1 = require("../validator");
const error_handler_1 = require("../error-handler");
const types_1 = require("../types");
async function removeVideoWatermark(params, client) {
    const rawInput = typeof params.videoUrl === "string" ? params.videoUrl.trim() : "";
    const extractedUrl = rawInput.match(/https?:\/\/[^\s]+/i)?.[0]?.replace(/[，。；;！!）)】\]]+$/, "") || rawInput;
    const normalizedParams = { ...params, videoUrl: extractedUrl };
    const validationError = (0, validator_1.validate)("removeVideoWatermark", normalizedParams);
    if (validationError)
        return validationError;
    const response = await client.post("/open/removeVideoWatermark", { videoUrl: extractedUrl }, types_1.TIMEOUT_CONFIG.videoWatermark);
    return response.code === types_1.ErrorCode.SUCCESS ? response : (0, error_handler_1.mapApiError)(response);
}
//# sourceMappingURL=remove-video-watermark.js.map