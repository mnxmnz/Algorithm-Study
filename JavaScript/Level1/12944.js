function solution(arr) {
  var answer = 0;
  var sum = 0;
  var length = arr.length;

  for (var i = 0; i < length; i++) {
    sum += arr[i];
  }

  answer = sum / length;

  return answer;
}

// 다른 사람 풀이 01
function average(array) {
  return array.reduce((a, b) => a + b) / array.length;
}

// 다른 사람 풀이 02
function average(array) {
  var sum = 0;
  for (var value of array) {
    sum += value;
  }
  return sum / array.length;
}
