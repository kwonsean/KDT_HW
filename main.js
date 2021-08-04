// 상품 데이터
const data = [
    { name: '초콜렛', price: 2000 },
    { name: '아이스크림', price: 1000 },
    { name: '컵라면', price: 1600 },
    { name: '볼펜', price: 2500 },
    { name: '아메리카노', price: 4000 },
    { name: '과자', price: 3000 },
    { name: '탄산수', price: 1200 },
    { name: '떡볶이', price: 3500 },
    { name: '노트', price: 1500 },
    { name: '껌', price: 500 }
];


// 사용자 입력 받기
const line = prompt('최대 금액을 입력해주세요.');
const amount = Number(line);


// 주어진 금액으로 살 수 있는 가장 비싼 상품을 구함
const item = getItemByAmount(data, amount);

const msg = item ? 
    `${amount}원으로 살 수 있는 가장 비싼 상품은 [${item.name}]이고, 가격은 ${item.price}원입니다.` :  //객체를 리턴해야함 
    '살 수 있는 상품이 없습니다.';

// 결과 출력
alert(msg);

// 아래에 getItemByAmount 함수를 작성하세요.
function getItemByAmount(data, amount){
    let change = 0;
    // 가장 작은 잔돈을 체크하기 위한 변수 선언
    let smallestChange = 9999999999;
    // 가장 작은 잔돈이 발생할때의 인덱스 값을 저장하기 위한 변수 선언
    let smallestChangeIndex = 0;

    // 먼저 입력값이 양수인지 확인 
    if(amount > 0){
        const result = data.filter(function (item, index, self){
            const PRICE = item.price;
            if (amount >= PRICE){
                change = amount - PRICE
                if(smallestChange > change){
                    smallestChange = change
                    smallestChangeIndex = index
                }
                //filter함수는 true인 값들을 배열속으로 모두 return하기 때문에 우선 최소잔돈이 초기화 될때마다 result배열에 return시행
                if (index == smallestChangeIndex ){
                    return self[smallestChangeIndex]
                }
        }
        });
        // result에는 최소 잔돈이 초기화 될때마다 객체의 형태로 배열에 추가가 되었으니 가장 마지막에 추가된 요소가 가장 작은 잔돈을 발생시키는 객체이다
        endGame = result.pop()
        return endGame
     
    } else{
        return null;
    }
};
