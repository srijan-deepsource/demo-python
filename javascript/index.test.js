const { addOne } = require(".")

describe('Test', () => {
  it('addOne', () => {
    expect(addOne(2)).toEqual(3)
  })
})
