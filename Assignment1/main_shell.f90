program name
    use point_module
    implicit none
    real(kind=8) :: pi
    character(len=100) :: arg
    integer :: n, ierr
    ! input no. of points as command line argument
    if(command_argument_count() /= 1) then
        print *, 'Usage: ./main_shell.x n'
        stop
    end if

    
    call get_command_argument(1,arg, ierr)

    read(arg, *) n

    ! estimate value of pi using n points
    pi = monte_carlo_pi(n)

    print *, pi

end program name