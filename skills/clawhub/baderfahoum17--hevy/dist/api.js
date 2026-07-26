/**
 * Hevy API Client
 *
 * REST client for the Hevy workout tracking API.
 * Docs: https://api.hevyapp.com/docs/
 */
const BASE_URL = "https://api.hevyapp.com";
export class HevyClient {
    apiKey;
    constructor(config) {
        this.apiKey = config.apiKey;
    }
    /**
     * Make an authenticated request to the Hevy API
     */
    async request(endpoint, options = {}) {
        const url = `${BASE_URL}${endpoint}`;
        const headers = {
            "api-key": this.apiKey,
            "Content-Type": "application/json",
            ...options.headers,
        };
        const response = await fetch(url, {
            ...options,
            headers,
        });
        if (!response.ok) {
            const text = await response.text();
            throw new Error(`Hevy API error ${response.status}: ${text}`);
        }
        // Handle empty responses (e.g., 204 No Content)
        const contentLength = response.headers.get("content-length");
        if (contentLength === "0" || response.status === 204) {
            return {};
        }
        return response.json();
    }
    // ============================================
    // Workouts
    // ============================================
    /**
     * Get paginated list of workouts
     * @param page Page number (1-indexed)
     * @param pageSize Items per page (max 10)
     */
    async getWorkouts(page = 1, pageSize = 10) {
        const params = new URLSearchParams({
            page: String(page),
            pageSize: String(Math.min(pageSize, 10)),
        });
        return this.request(`/v1/workouts?${params}`);
    }
    /**
     * Get all workouts (auto-paginate)
     */
    async getAllWorkouts() {
        const allWorkouts = [];
        let page = 1;
        let pageCount = 1;
        do {
            const response = await this.getWorkouts(page, 10);
            allWorkouts.push(...response.workouts);
            pageCount = response.page_count;
            page++;
        } while (page <= pageCount);
        return allWorkouts;
    }
    /**
     * Get a single workout by ID
     */
    async getWorkout(workoutId) {
        // API may return { workout: {...} } wrapper
        const response = await this.request(`/v1/workouts/${workoutId}`);
        return 'workout' in response ? response.workout : response;
    }
    /**
     * Get total workout count
     */
    async getWorkoutCount() {
        const response = await this.request("/v1/workouts/count");
        return response.workout_count;
    }
    /**
     * Get workout events since a date (for syncing)
     * @param since ISO 8601 date string
     */
    async getWorkoutEvents(since, page = 1, pageSize = 10) {
        const params = new URLSearchParams({
            page: String(page),
            pageSize: String(Math.min(pageSize, 10)),
            since,
        });
        return this.request(`/v1/workouts/events?${params}`);
    }
    /**
     * Create a new workout
     */
    async createWorkout(workout) {
        return this.request("/v1/workouts", {
            method: "POST",
            body: JSON.stringify(workout),
        });
    }
    /**
     * Update an existing workout
     */
    async updateWorkout(workoutId, workout) {
        return this.request(`/v1/workouts/${workoutId}`, {
            method: "PUT",
            body: JSON.stringify(workout),
        });
    }
    // ============================================
    // Routines
    // ============================================
    /**
     * Get paginated list of routines
     */
    async getRoutines(page = 1, pageSize = 10) {
        const params = new URLSearchParams({
            page: String(page),
            pageSize: String(Math.min(pageSize, 10)),
        });
        return this.request(`/v1/routines?${params}`);
    }
    /**
     * Get all routines (auto-paginate)
     */
    async getAllRoutines() {
        const allRoutines = [];
        let page = 1;
        let pageCount = 1;
        do {
            const response = await this.getRoutines(page, 10);
            allRoutines.push(...response.routines);
            pageCount = response.page_count;
            page++;
        } while (page <= pageCount);
        return allRoutines;
    }
    /**
     * Get a single routine by ID
     */
    async getRoutine(routineId) {
        const response = await this.request(`/v1/routines/${routineId}`);
        return response.routine;
    }
    /**
     * Create a new routine
     */
    async createRoutine(routine) {
        const response = await this.request("/v1/routines", {
            method: "POST",
            body: JSON.stringify(routine),
        });
        // API returns { routine: [Routine] }
        return response.routine[0];
    }
    /**
     * Update an existing routine
     */
    async updateRoutine(routineId, routine) {
        return this.request(`/v1/routines/${routineId}`, {
            method: "PUT",
            body: JSON.stringify(routine),
        });
    }
    // ============================================
    // Routine Folders
    // ============================================
    /**
     * Get paginated list of routine folders
     */
    async getRoutineFolders(page = 1, pageSize = 10) {
        const params = new URLSearchParams({
            page: String(page),
            pageSize: String(Math.min(pageSize, 10)),
        });
        return this.request(`/v1/routine_folders?${params}`);
    }
    /**
     * Get all routine folders (auto-paginate)
     */
    async getAllRoutineFolders() {
        const allFolders = [];
        let page = 1;
        let pageCount = 1;
        do {
            const response = await this.getRoutineFolders(page, 10);
            // API returns routine_folders or routines depending on if empty
            const folders = response.routine_folders ?? response.routines ?? [];
            allFolders.push(...folders);
            pageCount = response.page_count;
            page++;
        } while (page <= pageCount);
        return allFolders;
    }
    /**
     * Get a single routine folder by ID
     */
    async getRoutineFolder(folderId) {
        return this.request(`/v1/routine_folders/${folderId}`);
    }
    /**
     * Create a new routine folder
     */
    async createRoutineFolder(folder) {
        return this.request("/v1/routine_folders", {
            method: "POST",
            body: JSON.stringify(folder),
        });
    }
    // ============================================
    // Exercise Templates
    // ============================================
    /**
     * Get paginated list of exercise templates
     */
    async getExerciseTemplates(page = 1, pageSize = 10) {
        const params = new URLSearchParams({
            page: String(page),
            pageSize: String(Math.min(pageSize, 10)),
        });
        return this.request(`/v1/exercise_templates?${params}`);
    }
    /**
     * Get all exercise templates (auto-paginate)
     * Note: This can be a lot of data - Hevy has hundreds of built-in exercises
     */
    async getAllExerciseTemplates() {
        const allTemplates = [];
        let page = 1;
        let pageCount = 1;
        do {
            const response = await this.getExerciseTemplates(page, 10);
            allTemplates.push(...response.exercise_templates);
            pageCount = response.page_count;
            page++;
        } while (page <= pageCount);
        return allTemplates;
    }
    /**
     * Get a single exercise template by ID
     */
    async getExerciseTemplate(templateId) {
        return this.request(`/v1/exercise_templates/${templateId}`);
    }
    /**
     * Create a custom exercise template
     */
    async createExerciseTemplate(template) {
        return this.request("/v1/exercise_templates", {
            method: "POST",
            body: JSON.stringify(template),
        });
    }
    // ============================================
    // Exercise History
    // ============================================
    /**
     * Get exercise history for a specific exercise template
     * Returns all sets ever performed for this exercise
     */
    async getExerciseHistory(templateId, page = 1, pageSize = 10) {
        const params = new URLSearchParams({
            page: String(page),
            pageSize: String(Math.min(pageSize, 10)),
        });
        return this.request(`/v1/exercise_history/${templateId}?${params}`);
    }
    /**
     * Get all exercise history for a template (auto-paginate)
     */
    async getAllExerciseHistory(templateId) {
        const allHistory = [];
        let page = 1;
        let pageCount = 1;
        do {
            const response = await this.getExerciseHistory(templateId, page, 10);
            allHistory.push(...response.exercise_history);
            pageCount = response.page_count;
            page++;
        } while (page <= pageCount);
        return allHistory;
    }
    // ============================================
    // Utility Methods
    // ============================================
    /**
     * Search exercise templates by name
     */
    async searchExerciseTemplates(query) {
        const templates = await this.getAllExerciseTemplates();
        const lowerQuery = query.toLowerCase();
        return templates.filter(t => t.title.toLowerCase().includes(lowerQuery));
    }
    /**
     * Get recent workouts (shorthand for first page)
     */
    async getRecentWorkouts(limit = 5) {
        const response = await this.getWorkouts(1, Math.min(limit, 10));
        return response.workouts.slice(0, limit);
    }
    /**
     * Find exercise template by exact or partial name match
     */
    async findExerciseTemplate(name) {
        const templates = await this.searchExerciseTemplates(name);
        if (templates.length === 0)
            return null;
        // Prefer exact match
        const lowerName = name.toLowerCase();
        const exact = templates.find(t => t.title.toLowerCase() === lowerName);
        return exact ?? templates[0];
    }
}
