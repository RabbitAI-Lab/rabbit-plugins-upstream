export type PluginConfig = {
    apiKey?: string;
    baseUrl?: string;
};
export declare function readConfig(api: {
    config?: unknown;
}): PluginConfig;
export declare function callApi(cfg: PluginConfig, method: "GET" | "POST" | "PATCH" | "DELETE", path: string, options?: {
    body?: unknown;
    query?: Record<string, unknown>;
    signal?: AbortSignal;
}): Promise<unknown>;
