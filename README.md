# async_redis_queue


An asynchronous Redis Queue implemented using asyncio


## installation

```bash
$ pip install async_redis_queue

```

## use

```python

import asyncio
from async_redis_queue import create_async_redis_queue, AsyncRedisQueue


async def test1():
    q = await AsyncRedisQueue.from_cls_async('<queue-name>')
    return await q.get()

async def test2():
    q = await create_async_redis_queue('<queue-name>')
    await q.put('test')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

```

* Free software: MIT license



Features
--------

* TODO
