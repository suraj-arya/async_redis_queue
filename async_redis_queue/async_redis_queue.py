# -*- coding: utf-8 -*-

import aioredis
from zenpipeline.queues import BaseQueue


async def create_async_redis_queue(name, **kwargs):
    """
        Factory method to get an instance of
        AsyncRedisQueue asynchronously
    """
    instance = AsyncRedisQueue(name, **kwargs)
    await instance._init()
    return instance


class AsyncRedisQueue(BaseQueue):

    """
    Simple Queue with Redis Backend and asyncio_redis
    """

    def __init__(self, name, **kwargs):
        """
        The default connection parameters are: host='localhost', port=6379, db=0
        """

        self._db = None
        self.settings = kwargs
        self.key = name

    async def _init(self):
        host = self.settings.get('host', 'localhost')
        port = self.settings.get('port', 6379)

        self._db = await aioredis.create_connection(address=(host, port))

    @classmethod
    async def from_cls_async(cls, name, **settings):
        instance = cls(name, **settings)
        await instance._init()
        return instance

    async def qsize(self):
        """
        Return the approximate size of the queue.
        """
        return await self._db.execute('llen', self.key)

    async def is_empty(self):
        """
        Return True if the queue is empty, False otherwise.
        """
        return (await self.qsize()) == 0

    async def put(self, item):
        """
        Put item into the queue.
        """
        return await self._db.execute('rpush', self.key, item)

    async def get(self, block=True, timeout=None):
        """
        Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available.
        """
        if await self.is_empty():
            raise Exception('Queue is empty')

        item = await self._db.execute('lpop', self.key)

        return item.decode('ascii')
