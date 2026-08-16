"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.taskList = taskList;
const validator_1 = require("../validator");
const error_handler_1 = require("../error-handler");
const types_1 = require("../types");
async function taskList(params, client) {
    const { page, size } = (0, validator_1.normalizePageParams)(params);
    const apiResponse = await client.post("/open/taskList", { page: String(page), size: String(size) }, types_1.TIMEOUT_CONFIG.query);
    if (apiResponse.code !== types_1.ErrorCode.SUCCESS) {
        return (0, error_handler_1.mapApiError)(apiResponse);
    }
    return {
        code: types_1.ErrorCode.SUCCESS,
        message: apiResponse.message || "success",
        total: apiResponse.total,
        page,
        size,
        list: (apiResponse.list || []).map((item) => {
            const publicItem = { ...item };
            delete publicItem.x1;
            delete publicItem.y1;
            delete publicItem.x2;
            delete publicItem.y2;
            delete publicItem.mode;
            return publicItem;
        }),
    };
}
//# sourceMappingURL=task-list.js.map