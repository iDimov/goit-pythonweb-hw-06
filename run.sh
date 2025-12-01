#!/bin/bash

# Wrapper script для зручного запуску Python скриптів

VENV_PYTHON="/Users/vdim/Desktop/goit/6/.venv/bin/python"

case "$1" in
    seed)
        echo "Seeding database..."
        $VENV_PYTHON seed.py
        ;;
    demo)
        echo "Running demo..."
        $VENV_PYTHON demo.py
        ;;
    select)
        echo "Running queries..."
        $VENV_PYTHON my_select.py
        ;;
    test)
        echo "Testing all queries..."
        $VENV_PYTHON test_queries.py
        ;;
    cli)
        shift
        $VENV_PYTHON main.py "$@"
        ;;
    migrate)
        echo "Creating migration..."
        /Users/vdim/Desktop/goit/6/.venv/bin/alembic revision --autogenerate -m "${2:-Auto migration}"
        ;;
    upgrade)
        echo "Upgrading database..."
        /Users/vdim/Desktop/goit/6/.venv/bin/alembic upgrade head
        ;;
    *)
        echo "Usage: ./run.sh {seed|demo|select|test|cli|migrate|upgrade}"
        echo ""
        echo "Examples:"
        echo "  ./run.sh seed                                    # Seed database"
        echo "  ./run.sh demo                                    # Run demo"
        echo "  ./run.sh select                                  # Run basic queries"
        echo "  ./run.sh test                                    # Test all queries"
        echo "  ./run.sh cli -a list -m Teacher                  # CLI list teachers"
        echo "  ./run.sh cli -a create -m Teacher -n 'John Doe'  # CLI create teacher"
        echo "  ./run.sh migrate 'My migration'                  # Create migration"
        echo "  ./run.sh upgrade                                 # Apply migrations"
        exit 1
        ;;
esac
