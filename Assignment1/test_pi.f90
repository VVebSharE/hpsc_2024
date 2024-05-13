subroutine test_pi(n, input, output)
    use point_module

    integer, intent(in) :: n
    integer, intent(in) :: input(n)
    real(kind=8), intent(out) :: output(n)
    
    integer :: AcceptableError = 20 ! 20% error is acceptable
    real(kind=8) :: ActualPi = 3.14159

    real(kind=8) :: pi
    do i = 1, n
        pi = monte_carlo_pi(input(i))
        if((ABS(pi-ActualPi)/ActualPi)*100 > AcceptableError) then
            print *, "Not Acceptable estimate of pi", pi, "for", input(i) , " no of samples"
        end if
        output(i) = pi
    end do
    
end subroutine test_pi

