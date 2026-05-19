# Performance Checklist - Python

## Code Efficiency
- [ ] Use generators instead of lists for large datasets
- [ ] Profile with cProfile or py-spy
- [ ] Identify bottlenecks before optimizing
- [ ] Use list comprehensions over loops

## Database
- [ ] Add appropriate indexes
- [ ] Use connection pooling
- [ ] Avoid N+1 queries
- [ ] Batch operations when possible

## Async/Concurrency
- [ ] Use asyncio for I/O-bound operations
- [ ] Consider multiprocessing for CPU-bound tasks
- [ ] Monitor thread safety in concurrent code

## Caching
- [ ] Cache expensive computations (functools.lru_cache)
- [ ] Use Redis for distributed caching
- [ ] Set appropriate TTLs
