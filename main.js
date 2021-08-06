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

    // 먼저 입력값이 양수인지 확인 
    if(amount > 0){
        // 입력값보다 물건가격이 작은 객체들을 걸러서 result에 객체를 담은 배열 형식으로 담아준다.
        const uCanBuy = data.filter( data_item =>  {if(amount - data_item.price >= 0) return data_item});

        // 살 수 있는 물건들을 모아둔 배열에서 가격만을 뽑아 새로운 배열을 만들어 준다.
        const priceList = uCanBuy.map(CanBuyItem => CanBuyItem.price)

        // 가격만 들어있는 배열에서 가장 큰수를 찾아 그 수의 index값을 id변수에 넣어준다. 
        const id = priceList.indexOf(Math.max(...priceList))
        
        // 가장 비싼 가격을 가지는 물건의 index값을 살 수 있는 물건들을 모아둔 배열에 넣어 객체를 리턴해 준다.
        return uCanBuy[id]
     
    } else{
        return null;
    }
};
