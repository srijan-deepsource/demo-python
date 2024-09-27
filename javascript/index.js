function addOne(a) {
  if (typeof a === 'number') {
    return a + 1
  } else {
    throw new Error(`${a} is not a number`)
  }
}

function subOne(a) {
  if (typeof a === 'number') {
    return a - 1
  } else {
    throw new Error(`${a} is not a number`)
  }
}

module.exports = {
  addOne,
  subOne
}