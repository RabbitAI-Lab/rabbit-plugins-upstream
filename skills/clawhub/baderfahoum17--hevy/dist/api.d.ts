/**
 * Hevy API Client
 *
 * REST client for the Hevy workout tracking API.
 * Docs: https://api.hevyapp.com/docs/
 */
import type { HevyConfig } from "./config.js";
import type { Workout, WorkoutsResponse, WorkoutEventsResponse, Routine, RoutinesResponse, RoutineFolder, RoutineFoldersResponse, ExerciseTemplate, ExerciseTemplatesResponse, ExerciseHistoryResponse, CreateWorkoutRequest, CreateRoutineRequest, UpdateRoutineRequest, CreateRoutineFolderRequest, CreateExerciseTemplateRequest } from "./types.js";
export declare class HevyClient {
    private apiKey;
    constructor(config: HevyConfig);
    /**
     * Make an authenticated request to the Hevy API
     */
    private request;
    /**
     * Get paginated list of workouts
     * @param page Page number (1-indexed)
     * @param pageSize Items per page (max 10)
     */
    getWorkouts(page?: number, pageSize?: number): Promise<WorkoutsResponse>;
    /**
     * Get all workouts (auto-paginate)
     */
    getAllWorkouts(): Promise<Workout[]>;
    /**
     * Get a single workout by ID
     */
    getWorkout(workoutId: string): Promise<Workout>;
    /**
     * Get total workout count
     */
    getWorkoutCount(): Promise<number>;
    /**
     * Get workout events since a date (for syncing)
     * @param since ISO 8601 date string
     */
    getWorkoutEvents(since: string, page?: number, pageSize?: number): Promise<WorkoutEventsResponse>;
    /**
     * Create a new workout
     */
    createWorkout(workout: CreateWorkoutRequest): Promise<Workout>;
    /**
     * Update an existing workout
     */
    updateWorkout(workoutId: string, workout: CreateWorkoutRequest): Promise<Workout>;
    /**
     * Get paginated list of routines
     */
    getRoutines(page?: number, pageSize?: number): Promise<RoutinesResponse>;
    /**
     * Get all routines (auto-paginate)
     */
    getAllRoutines(): Promise<Routine[]>;
    /**
     * Get a single routine by ID
     */
    getRoutine(routineId: string): Promise<Routine>;
    /**
     * Create a new routine
     */
    createRoutine(routine: CreateRoutineRequest): Promise<Routine>;
    /**
     * Update an existing routine
     */
    updateRoutine(routineId: string, routine: UpdateRoutineRequest): Promise<Routine>;
    /**
     * Get paginated list of routine folders
     */
    getRoutineFolders(page?: number, pageSize?: number): Promise<RoutineFoldersResponse>;
    /**
     * Get all routine folders (auto-paginate)
     */
    getAllRoutineFolders(): Promise<RoutineFolder[]>;
    /**
     * Get a single routine folder by ID
     */
    getRoutineFolder(folderId: number): Promise<RoutineFolder>;
    /**
     * Create a new routine folder
     */
    createRoutineFolder(folder: CreateRoutineFolderRequest): Promise<RoutineFolder>;
    /**
     * Get paginated list of exercise templates
     */
    getExerciseTemplates(page?: number, pageSize?: number): Promise<ExerciseTemplatesResponse>;
    /**
     * Get all exercise templates (auto-paginate)
     * Note: This can be a lot of data - Hevy has hundreds of built-in exercises
     */
    getAllExerciseTemplates(): Promise<ExerciseTemplate[]>;
    /**
     * Get a single exercise template by ID
     */
    getExerciseTemplate(templateId: string): Promise<ExerciseTemplate>;
    /**
     * Create a custom exercise template
     */
    createExerciseTemplate(template: CreateExerciseTemplateRequest): Promise<ExerciseTemplate>;
    /**
     * Get exercise history for a specific exercise template
     * Returns all sets ever performed for this exercise
     */
    getExerciseHistory(templateId: string, page?: number, pageSize?: number): Promise<ExerciseHistoryResponse>;
    /**
     * Get all exercise history for a template (auto-paginate)
     */
    getAllExerciseHistory(templateId: string): Promise<ExerciseHistoryResponse["exercise_history"]>;
    /**
     * Search exercise templates by name
     */
    searchExerciseTemplates(query: string): Promise<ExerciseTemplate[]>;
    /**
     * Get recent workouts (shorthand for first page)
     */
    getRecentWorkouts(limit?: number): Promise<Workout[]>;
    /**
     * Find exercise template by exact or partial name match
     */
    findExerciseTemplate(name: string): Promise<ExerciseTemplate | null>;
}
