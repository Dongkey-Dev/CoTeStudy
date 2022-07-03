from a_test_m import find_users_sync, find_users_async, use_async
import time
import asyncio

async def main():
    start = time.time()
    result = await asyncio.wait([
        use_async(i) for i in range(1,4)
    ])
    print("소요시간 : ", time.time() - start)
    print("result : ", result)
    
if __name__ == "__main__":
    asyncio.run(main())