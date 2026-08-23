"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.removeImageWatermark = removeImageWatermark;
const validator_1 = require("../validator");
const error_handler_1 = require("../error-handler");
const types_1 = require("../types");
async function removeImageWatermark(params, client) {
    const validationError = (0, validator_1.validate)("removeImageWatermark", params);
    if (validationError)
        return validationError;
    const file = params.file;
    const requestParams = {
        sync: String(params.sync ?? true),
    };
    if (params.operationId != null && String(params.operationId).trim() !== "") {
        requestParams.operationId = String(params.operationId).trim();
    }
    const response = await client.upload("/open/removeImageWatermark", requestParams, { name: file.name, data: file.data ?? file }, types_1.TIMEOUT_CONFIG.imageWatermark);
    return response.code === types_1.ErrorCode.SUCCESS ? response : (0, error_handler_1.mapApiError)(response);
}
//# sourceMappingURL=remove-image-watermark.js.map