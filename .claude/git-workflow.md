# Git Workflow

## Branching Strategy: Trunk-Based Development

### Branch Types
- **main** - Production-ready code, always deployable
- **feature/** - New features (short-lived, e.g., feature/user-auth)
- **fix/** - Bug fixes (short-lived, e.g., fix/login-bug)
- **docs/** - Documentation updates

### Workflow

1. **Create a branch from main**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/feature-name
   ```

2. **Make commits with clear messages**
   ```bash
   git commit -m "Add user authentication flow"
   ```

3. **Keep branch up-to-date**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

4. **Push and create PR**
   ```bash
   git push origin feature/feature-name
   ```

5. **Code review and merge**
   - Get at least 1 approval
   - Merge to main via PR (delete branch after)

6. **Deploy**
   - main is always deployable
   - Tag releases: git tag v1.0.0

### Commit Message Format
```
[type]: Brief description

Optional longer explanation if needed.

Closes #123
```

Types: feat, fix, docs, refactor, test, chore

### Best Practices
- Keep branches short-lived (< 3 days)
- Small, focused PRs (< 400 lines changed)
- Rebase before merging (not merge commits)
- Delete branches after merging
