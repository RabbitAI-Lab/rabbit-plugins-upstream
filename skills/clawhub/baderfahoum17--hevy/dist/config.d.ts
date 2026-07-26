/**
 * Configuration management for Hevy CLI
 *
 * API key is read from HEVY_API_KEY environment variable.
 * No file-based config needed - keeps things simple and secure.
 */
export interface HevyConfig {
    apiKey: string;
}
/**
 * Get API key from environment variable
 */
export declare function getApiKey(): string | null;
/**
 * Check if API key is configured
 */
export declare function isConfigured(): boolean;
/**
 * Require API key or exit with helpful message
 */
export declare function requireApiKey(): string;
/**
 * Get config object (for API client)
 */
export declare function getConfig(): HevyConfig;
