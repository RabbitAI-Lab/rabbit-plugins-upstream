"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.imageWatermarkTaskDetail = imageWatermarkTaskDetail;
const validator_1 = require("../validator");
const error_handler_1 = require("../error-handler");
const types_1 = require("../types");
async function imageWatermarkTaskDetail(params, client) {
    const validationError = (0, validator_1.validate)("imageWatermarkTaskDetail", params);
    if (validationError)
        return validationError;
    const response = await client.post("/open/imageWatermarkTaskDetail", { taskId: params.taskId }, types_1.TIMEOUT_CONFIG.query);
    return response.code === types_1.ErrorCode.SUCCESS ? response : (0, error_handler_1.mapApiError)(response);
}
//# sourceMappingURL=image-watermark-task-detail.js.map