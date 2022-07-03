import time
import asyncio

async def find_users_async(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        await asyncio.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')
    
def find_users_sync(n):
    for i in range(1, n + 1):
        print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
        time.sleep(1)
    print(f'> 총 {n} 명 사용자 동기 조회 완료!')    
    
async def use_async(n):
    result = []
    for i in range(1, n+1):
        print(f'{i}_processing..')
        await asyncio.sleep(1)
        result.append(i)
    return result
        