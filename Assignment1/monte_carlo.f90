program main2
    implicit none
    integer :: n = 8
    real(kind=8) :: output(8)
    integer :: input(8)
    input = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
    print *, "Testing pi"

    call test_pi(n, input, output)
    print *, "No. of Samples: ", input
    print *, "Estimated value of pi: ", output

end program main2